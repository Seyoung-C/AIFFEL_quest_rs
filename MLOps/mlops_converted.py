#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import wandb
from wandb.integration.keras import WandbMetricsLogger
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import numpy as np


# In[2]:


wandb.login(key= "513c4269349cec2cb6b8c9019721be7de2fdfa8b")


# In[3]:


# Wandb 설정
WANDB_PROJECT = "MLOps"
WANDB_ENTITY = "seyoung-c-chung-ang-university"


# In[4]:


def load_and_preprocess_data():
    # TensorFlow.keras로 MNIST 데이터셋 로드
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # 데이터 정수형에서 실수형으로 변환하고 정규화 (0에서 1 사이로 스케일링)
    x_train, x_test = x_train.astype('float32') / 255.0, x_test.astype('float32') / 255.0

    # 채널 차원을 추가하여 형상 일치 (예: (28, 28) -> (28, 28, 1))
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    return (x_train, y_train), (x_test, y_test)


# In[5]:


from tensorflow.keras import layers, models, optimizers

def create_model(learning_rate=0.001, conv1_filters=32, conv2_filters=64):
    """간단한 CNN 모델 생성"""
    model = models.Sequential()
    
    # 첫 번째 컨볼루션 층
    model.add(layers.Conv2D(conv1_filters, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    
    # 두 번째 컨볼루션 층
    model.add(layers.Conv2D(conv2_filters, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    
    # 완전 연결층
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))  # MNIST는 10개의 클래스
    
    # 모델 컴파일
    model.compile(optimizer=optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model


# In[9]:


def train_model(**context):
    """모델 학습 및 W&B 로깅"""
    # W&B 초기화
    wandb.init(
        project=WANDB_PROJECT,
        entity=WANDB_ENTITY,
        config={
            "learning_rate": 0.001,
            "conv1_filters": 32,
            "conv2_filters": 64,
            "batch_size": 128,
            "epochs": 10
        }
    )
    
    # 데이터 로드
    (x_train, y_train), (x_test, y_test) = load_and_preprocess_data()
    
    # 모델 생성
    model = create_model(
        learning_rate=wandb.config.learning_rate,
        conv1_filters=wandb.config.conv1_filters,
        conv2_filters=wandb.config.conv2_filters
    )
    
    # 모델 학습
    model.fit(
        x_train, y_train,
        epochs=wandb.config.epochs,
        batch_size=wandb.config.batch_size,
        validation_data=(x_test, y_test),
        callbacks=[WandbMetricsLogger()]
    )
    
    # 모델 평가
    test_loss, test_accuracy = model.evaluate(x_test, y_test)
    print(f"Test accuracy: {test_accuracy}")
    
    # W&B에 최종 메트릭 기록 (test_loss, test_accuracy)
    wandb.log({
        "test_loss": test_loss,
        "test_accuracy": test_accuracy
    })
    
    # 모델 저장
    model.save(f"mnist_model_{datetime.now().strftime('%Y%m%d_%H%M%S')}.keras")
    
    wandb.finish()


# In[7]:


def hyperparameter_sweep():
    """W&B를 사용한 하이퍼파라미터 튜닝"""
    sweep_config = {
        'method': 'random',
        'metric': {'name': 'val_accuracy', 'goal': 'maximize'},
        'parameters': {
            'learning_rate': {'values': [0.001, 0.01, 0.0001]},
            'conv1_filters': {'values': [16, 32, 64]},
            'conv2_filters': {'values': [32, 64, 128]},
            'batch_size': {'values': [64, 128, 256]}
        }
    }
    
    sweep_id = wandb.sweep(sweep_config, project=WANDB_PROJECT)
    wandb.agent(sweep_id, train_model, count=5)


# In[10]:


# Airflow DAG 정의

import pendulum  # Airflow는 pendulum을 사용합니다

local_tz = pendulum.timezone("Asia/Seoul")  # 한국 시간대 사용

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1, tzinfo=local_tz),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}



dag = DAG(
    'mnist_training_pipeline',
    default_args=default_args,
    description='MNIST_training',
    schedule = '@daily',
    catchup=False
)

# DAG 태스크 정의
preprocessing_task = PythonOperator(
    task_id='load_and_preprocess_data',
    python_callable=load_and_preprocess_data,
    do_xcom_push=False,
    dag=dag
)

training_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    do_xcom_push=False,
    dag=dag
)

hyperparameter_tuning_task = PythonOperator(
    task_id='hyperparameter_tuning',
    python_callable=hyperparameter_sweep,
    do_xcom_push=False,
    dag=dag
)

# 태스크 의존성 설정
preprocessing_task >> training_task >> hyperparameter_tuning_task

# Jupyter Notebook에서 직접 실행하기 위한 코드
if __name__ == "__main__":
    # 단일 실험 실행
    train_model()

    hyperparameter_sweep()


# In[12]:


execution_date = datetime(2024, 11, 10, tzinfo=local_tz)
dag.test(execution_date=execution_date)
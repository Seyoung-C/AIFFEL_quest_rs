# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 최세영
- 리뷰어 : 이치오

# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - ResNet-34, ResNet-50 모델 구현이 정상적으로 진행되었는가?
    - ![image](https://github.com/user-attachments/assets/7f9d0bb0-c908-449a-abf5-a698a782fea7)
    - 구현한 ResNet 모델을 활용하여 Image Classification 모델 훈련이 가능한가?
    - ![image](https://github.com/user-attachments/assets/a834b737-510f-48a3-9794-cf0788a2e1ba)
    - Ablation Study 결과가 바른 포맷으로 제출되었는가?
    - ![image](https://github.com/user-attachments/assets/9870ef40-2b2e-4420-b052-b48ab3a98cca)
    
- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 새롭게 cats vs dogs를 import 하는 법을 잘 설명해 두었다
    - ![image](https://github.com/user-attachments/assets/32d9bc71-a31b-4920-bd78-9089e3a10e27)
        
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 사진 압축률에 따른 학습 지표, 시간 차이를 비교함
    - ![image](https://github.com/user-attachments/assets/acf5a5b0-a6c8-4253-a655-350f526a125f)
        
- [x]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해 배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - ![image](https://github.com/user-attachments/assets/de73433e-3ee5-4e18-b99e-629a669a19e9)
        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
    - ![image](https://github.com/user-attachments/assets/249f69e3-8218-4192-a00b-eebc31d5133a)

# 회고(참고 링크 및 코드 개선)
사진 파일 압축률에 따른 모델 학습 속도와 성능 차를 비교한 점과 repetition 수와 model name을 설정할때 '''x if condition(x) else y''' 문을 이용해 코드의 중복을 줄인 점 또한 인상깊었다.

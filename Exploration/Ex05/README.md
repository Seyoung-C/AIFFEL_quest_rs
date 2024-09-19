# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 최세영
- 리뷰어 : 윤철희


# PRT(Peer Review Template)
- [ o ]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**

  ![image](https://github.com/user-attachments/assets/4bd5a234-eb9c-4f4a-aaac-e06cba5b7a26)

  ![image](https://github.com/user-attachments/assets/7c5826d9-9720-4e38-9ad6-b81ea9960cc4)

  ![image](https://github.com/user-attachments/assets/fef5d11e-842a-48ae-a948-cf4f3bb76eac)


    3가지 모델 모두 학습과 accuacy를 완성 해주셨습니다.


  ![image](https://github.com/user-attachments/assets/37eb436e-e66b-4bb3-925e-ae7127b7d6f2)

    학습된 Embedding 부분도 word2vec으로 오류없이 완성 해주셨습니다. 

          
    
- [ o ]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**

  ![image](https://github.com/user-attachments/assets/ca53cb8f-782f-4530-91cb-a56839b01494)

    함수의 용도가 어떠한 동작을 하는지 주석으로 잘 설명해주셨습니다. 

        
        
- [ o ]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**

    ![image](https://github.com/user-attachments/assets/a5fc9197-c617-459b-a907-36e8c5455f7a)

    
    # 처음 몇 개 인덱스는 사전에 정의되어 있습니다.
    word_to_index["<PAD>"] = 0
    word_to_index["<BOS>"] = 1
    word_to_index["<UNK>"] = 2  # unknown
    word_to_index["<UNUSED>"] = 3

    이부분을 작성하시지 않았을 때 padding 부분에서 오류가 발생한 점을 위의 코드을 추가하여 해결 하였습니다. 
    
- [ o ]  **4. 회고를 잘 작성했나요?**
    ![image](https://github.com/user-attachments/assets/9f716944-bfa8-4b99-9558-59f3a9d4e4ae)

    
        
- [ o ]  **5. 코드가 간결하고 효율적인가요?**
    ![image](https://github.com/user-attachments/assets/157c3820-8ad5-4dad-bc74-f0a8b50dccb5)

    함수를 사용해서 불필요한 코드 작성을 하지 않으셨습니다. 

# 회고(참고 링크 및 코드 개선)

 노드에서는 안나와있었지만 word2vec의 하이퍼파라미터 중 window size나 sliding window를 추가하면 성능을 더 올릴 수 있을거 같아요
 layer 층과 규제를 더 하는 것도 하나의 방법이라고 생각합니다. 
 2시간 동안 되게 많은 에러들을 해결해나가서 머리가 아프시겠지만 2% 정도면 85% 달성 하실 수 있어요 힘내세요

 word2vec window_size 참고 : https://www.tensorflow.org/text/tutorials/word2vec
 

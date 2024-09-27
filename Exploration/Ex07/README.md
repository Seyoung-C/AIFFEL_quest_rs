# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 최세영
- 리뷰어 : 오수연


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - <img width="602" alt="image" src="https://github.com/user-attachments/assets/84bdb474-2b39-4b5f-ab74-07a36ba1ec69">
        - 문맥에 맞는 답변을 잘 하는 것 같습니다.
    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - <img width="756" alt="image" src="https://github.com/user-attachments/assets/a98aa3bc-525c-4d2f-ad3e-b8851438fd40">
    - 데이터 전처리 부분에서 이해하기 쉽게 글로 따로 설명 해주셨습니다.
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - <img width="208" alt="image" src="https://github.com/user-attachments/assets/b28ab5d3-8c27-4904-a341-85e310a89ab6">
    - 새로운 시도로 MAX_LENGTH =8 
    - 시퀀스 길이 평균이 8이여서 변경해서 진행하셨다고 설명해주셨습니다.
        
- [O]  **4. 회고를 잘 작성했나요?**
    - <img width="709" alt="image" src="https://github.com/user-attachments/assets/60aa8856-a9d1-456a-97eb-ca32cdd27a6a">
    - dropout과 max_length를 조절해서 acc를 올린 것을 기록
        - (신기하게도 max_length가 줄어들 수록 acc가 올랐고, dropout은 0.1, 0.2, 0.3으로 커짐에 따라 acc도 올라갔습니다.)
    - 추가적으로 어떤 방향으로 더 연구해볼 수 있을지도 기입해주셨습니다.
        - 데이터 증강을 사용하거나, 학습률을 조정하고, 배치 크기를 조절하거나, 가중치를 초기화하는 등 다른 하이퍼 파라미터를 수정하면 더 좋은 성능을 내지 않을까 싶습니다.
        - 혹은 정규화 기법을 사용하고, feature engineering 기술이 들어가면 더욱 좋은 모델성능을 보이지 않을까 싶습니다.
        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - <img width="614" alt="image" src="https://github.com/user-attachments/assets/10d3d2af-e9ce-4f21-aed1-756f5318e7b1">
    - 거의 대부분 함수화 하여 깔끔하게 구현하였습니다.


# 회고(참고 링크 및 코드 개선)
```
리뷰 해주시면서 느꼈던 성능의 아쉬움은 저도 느꼈던 부분이라 공감됐습니다.
추가적인 성능 향상을 위해 방법 고민하시는 것도 인상 깊었습니다.
저도 추후에는 성능향상을 위한 방법도 더 고민해봐야겠습니다. 
```


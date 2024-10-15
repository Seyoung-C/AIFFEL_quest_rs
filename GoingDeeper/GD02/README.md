# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 최세영
- 리뷰어 : 오수연


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - <img width="400" alt="image" src="https://github.com/user-attachments/assets/9911849a-8b3f-4c36-82c7-b275a0b1eb30">
    - <img width="400" alt="image" src="https://github.com/user-attachments/assets/5dd3a97f-734c-4d52-ae58-d4c7d6ba1e4d">
        - 증강 전후의 비교 시각화 
    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - <img width="691" alt="image" src="https://github.com/user-attachments/assets/abca9a72-9d83-4ab5-a332-7967f617c1a2">
    - Early stopping 넣은것도 궁금했는데 해당 자료 바탕으로 추가학습을 더 진행 후 사용해봐야겠습니다.
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - <img width="716" alt="image" src="https://github.com/user-attachments/assets/5ae922a2-9eec-4213-82a9-e2b4379d24e5">
    - 원핫인코딩에서 SparseCategoricalCrossentropy을 사용하면 에러난 부분에 대해서 기록하였습니다.
        - categorical_crossentropy 사용하므로 디버깅도 완료
        
- [O]  **4. 회고를 잘 작성했나요?**
    - <img width="730" alt="image" src="https://github.com/user-attachments/assets/957a442f-3df2-4ac3-ba15-093c6bc2b70c">
    - 추가적으로 어떤 부분을 시도했었는지 볼 수 있었습니다. 
        - 아이디어가 좋아보여서 추후에 적용해보려고 합니다
        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - <img width="592" alt="image" src="https://github.com/user-attachments/assets/afdf32b2-9205-483d-bce8-ca64422591eb">
    - 최대한 정리해서 깔끔한 코드를 만들려고 하셨던거 같습니다.


# 회고(참고 링크 및 코드 개선)
```
성능 올리려고 ReduceLROnPlateau / Rotation, Zoom, Shift 증강 추가/ Drop out 추가 / L1, L2규제 넣기 / Batch Normalization 추가/ Optimizer Adam으로 변경 / Transfer Learning 활용으로 특정 레이어 학습에 추가
-> 짧은 시간 내에 다양한 시도들을 진행보신거에 놀랬습니다. 항상 추가 실험까지 진행하시려는 도전이 멋있는거 같습니다
```


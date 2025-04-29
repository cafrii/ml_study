
# 위키독스: 랭체인(LangChain) 입문부터 응용까지

https://wikidocs.net/book/14473



## 이 책 연습 전용 가상환경
```
conda env list
conda create -n ml_langchain python=3.9
conda activate ml_langchain
pip install -U pip
conda install ipykernel
```

그 다음 각 챕터에서 필요한 패키지는 노트북 맨 위에서 각각 설명함.

### 주의 사항
- openai api key는 무료로 받을 수 있는 방법이 없는 모양인지, quota limit 에 걸려서 동작 안함.
- google gemini api key는 rate limit 가 있긴 하지만 연습에 사용할 수준은 됨.
  - 따라서 앞으로 이 연습 노트에서의 llm api 는 gemini 로 진행하기로 함.



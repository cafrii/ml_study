



## URLs

- 저자가 직접 관리하는 github repo
  - https://github.com/phdshinai/ANN_DL101

- ann: 인공신경망 기초
  - https://www.youtube.com/playlist?list=PLfGJDDf2OqlSAL9kE4FvT_rG4DH_8S4AQ

- deeplearning: Deep Leaning 101
  - https://www.youtube.com/playlist?list=PLfGJDDf2OqlQkHqKB7uonQGeNRfUo_TMe

- ml-for-ai: 인공지능을 위한 머신러닝 101
  - https://www.youtube.com/playlist?list=PLfGJDDf2OqlQFAC87V3lmefyUcz_htJ9W

- 구글 문서 정리 중..
  - https://docs.google.com/document/d/12RXpiGVEMaCH8jHuGTuSlwbSGZ2wbKjqGghRPL7G7ug/edit?tab=t.8ft17o66q8f6



## Artificial Neural Network (ANN)

### 나만의 퍼셉트론을 만들어보자

- https://www.youtube.com/watch?v=YODTXF9OIiw&list=PLfGJDDf2OqlSAL9kE4FvT_rG4DH_8S4AQ&index=10
- ann-04-1st-perceptron.ipynb




## Deep Learning 101


## Machine Learning 101


## TIPs
요즘 유행하는 uv 로 가상환경 만들고 vs code 에서 노트북 실행하기

만들고자 하는 서브 폴더에서 직접 uv project 생성
```
cd <subfolder>
uv init .
uv add --dev ipykernel
code . # 또는 cursor .
```
이렇게 해서 실행된 vs code 에서는 *.ipynb 노트북 파일을 열고 나서
우 상단 '커널 선택'을 누를 경우, Python Environment 목록에 다음과 같이 권장 환경으로 방금 생성한 가상 환경이 인식되어 표시된다. 이것을 그냥 선택하면 된다.
```
* .venv (Python 3.x.y) .venv/bin/python
기타 다른 가상 환경들..
```
이렇게 vs code가 커널에 연결되면, vs code 에서 '새 터미널'을 띄울 때에도 알아서 `.venv/bin/activate` 를 실행해 주기 때문에 터미널도 모두 가상 환경에서 동작된다.

대체로 다음과 같은 패키지들이 필요할 것이다.
```
uv add ipykernel torch torchvision matplotlib
```
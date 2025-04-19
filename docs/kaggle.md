
## kaggle 노트북을 로컬에서 실행하는 방법

- 먼저 kaggle 전용 환경을 생성하는 것이 좋다.
- kaggle 이라는 이름의 conda 가상 환경을 생성하자. 다른 가상 환경이라도 상관 없을 것임.
```
conda deactivate
conda env list
  ..
  base                   /Users/yhlee/miniforge3
  ml                     /Users/yhlee/miniforge3/envs/ml

conda create -n kaggle python=3.9
conda env list
  ..
  kaggle                 /Users/yhlee/miniforge3/envs/kaggle
  ..

conda activate kaggle
(kaggle)
```

- notebook 서버를 설치한다.
  - kaggle 에서는 가급적 pip 만을 사용하도록 하자.
  - 이 밖에도 여러 패키지가 필요할 수 있지만, 모두 노트북 안에서 수행할 수 있으니, 지금 당장은 이것만 있으면 된다.
```
conda install jupyter notebook
```

- 노트북 서버를 실행한다.
  - 주의: 실행시키는 현재 폴더가 중요하다. 현재 노트북에서의 작업 폴더가 되는데, 모든 다운로드 받는 파일이 저장되므로, git 저장소의 ignored 처리 된 곳에서 하는 것이 좋다.
```
mkdir -p _work && cd _work
jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --NotebookApp.port_retries=0
```

- 노트북 서버 실행 후 콘솔에 표시된 내용 중에, 다음과 같이 접속 URL 을 알려주는 부분을 찾아야 한다.
```
...
[I 2025-04-19 10:57:01.109 ServerApp] Jupyter Server 2.15.0 is running at:
[I 2025-04-19 10:57:01.109 ServerApp] http://localhost:8888/tree?token=008e596ac8c9c350d5ff7856cf5ce2e7e6ffb23bc933785a
[I 2025-04-19 10:57:01.109 ServerApp]     http://127.0.0.1:8888/tree?token=008e596ac8c9c350d5ff7856cf5ce2e7e6ffb23bc933785a
[I 2025-04-19 10:57:01.109 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```

## 특정 competition 에 참여하고자 하는 경우

웹페이지에서 규칙 동의 절차를 진행해야 한다. 그런데 이 과정은 CLI 에서는 할 수 없다.

예를 들어, 노트북에서 다음을 실행한다는 것은 'paddy-disease-classification' 대회의 데이터를 받는 것이고, 그럴려면 해당 대회 페이지에 접속해서 규칙에 동의를 해야 한다.
```
comp = 'paddy-disease-classification'
path = setup_comp(comp, install='fastai "timm>=0.6.2.dev0"')
```

### 규칙 동의 절차

- kaggle 사이트에서 대회 이름으로 검색하면 대회 페이지를 찾을 수 있다. 아래는 위 예시의 'paddy-disease-classification' 대회의 페이지이다.

  - https://www.kaggle.com/c/paddy-disease-classification/overview

- 맨 우측 탭에 Rules 버튼을 눌러 동의 절차를 확인할 수 있다. 페이지 아래에 "Late Submission" 버튼을 누른다.
(이미 종료된 대회 이므로 'Late' 라고 하는 듯)

- 팝업 창이 뜨고, 규칙에 대한 내용이 표시됨. 읽고 난 후 맨 아래 "I Understand and Accept" 버튼 누름.

- 그러면 이 대회 페이지에 다음과 같이 표시가 추가됨.
  - "You have accepted the rules for this competition. Good luck!"




## kaggle 데이터 예시

- `setup_comp(..)` 를 호출하면 다운로드 받아지는 파일
  - paddy-disease-classification.zip
  - 약 1GB 에 달하는 큰 파일이다.
  - 위 파일이 압축 해제 되면 더 커짐.


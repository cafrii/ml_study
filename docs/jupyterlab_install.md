

## jupyter notebook 용 패키지

일부 문서에선 notebook 을 설치하라고 설명하고 있고, 반면 다른 곳에선 jupyterlab 을 설치하라고 안내한다.

jupyter notebook 은 기존의 노트북 인터페이스를 실행하는 패키지이고, jupyterlab 은 최신 웹 기반 인터랙티브 개발 환경이다.

jupyterlab 은 노트북, 터미널, 텍스트 편집기 등을 통합하여 더욱 강력한 개발 환경을 제공한다.
최신 기능과 향상된 사용자 경험을 위해 jupyterlab 을 사용하는 것이 추천된다.


그런데 어차피 웹 인터페이스가 아니라 vscode 에서 작업할 거라면, 어떤 방식이든 상관 없다.


### notebook 설치 및 실행

```
# 가상환경 활성화
conda activate ml

# 설치
conda install jupyter notebook
```

### notebook 서버 실행
```
jupyter notebook
```


### jupyterlab 설치
```
conda install jupyterlab
```


### jupyterlab 실행
```
jupyterlab
```


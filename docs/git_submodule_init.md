
## 서브모듈 등록

아래는 처음 서브모듈 등록했던 작업 내역임. 새로 clone 받을 땐 git clone 옵션에 --recurse-submodules 를 넣어서 사용하면 됨.

참고
- https 대신 ssh 를 사용하고 있으니 주의.
- 또한 top repo 에서는 sub repo 와 동기화 안시킬 것임.

### llm book

1: llm book 저자가 관리하는 repo 를 fork 하고, 웹 페이지에서 확인한다.
https://github.com/cafrii/llm-onlybooks

이 repo 에 서브 모듈 추가한다.

```
cd <tensorflow_study_workdir>
git submodule add git@github.com:cafrii/llm-onlybooks.git
```

.gitmodules 파일이 생성됨을 확인한다.
```
[submodule "llm-onlybooks"]
	path = llm-onlybooks
	url = git@github.com:cafrii/llm-onlybooks.git
```

혹시 기존에 local 에 클론해 작업하고 있던게 있다면, 여기로 이동.
```
git remote add myoldwc ~/work/somewhere
git remote -v
git fetch myoldwc
```

#### 문제점

맥에서 클론 받으니, 폴더 이름의 자소가 분리 표현되어 모든 파일이 untracked 라고 보임.
적어도 이 llmbook 리포는 맥에서는 건드리지 않는게 좋겠음.


### neowizard

마찬가지로 github web 에서 fork

문제가 하나 있음. 이 neowizard 리포에는 몇 개의 폴더들이 있는데, 일단 당장은 TensorFlow2 폴더만 관심이 있음.

```
276K	DataAnalysis
 13M	DeepLearningProject
271M	MachineLearning
 23M	PyTorch
 25M	TensorFlow2
```

그래서 TensorFlow2 폴더만 sparse 로 가져옴..

```
git clone --depth=1 --filter=blob:none --sparse git@github.com:cafrii/neowizard.git neo-tensorflow2

cd neo-tensorflow2

git sparse-checkout set TensorFlow2

git pull origin master
```

이 폴더는 좀 특수하게 체크아웃을 한 관계로, 굳이 submodule 로 등록을 해야 할 필요가 있을까 싶긴 한데... 일단 등록은 함.

```
cd .. # 상위 탑 프로젝트

git submodule add git@github.com:cafrii/neowizard.git neo-tensorflow2

# git submodule absorbgitdirs # 굳이 하진 않음.
```

#### 2025/3/13, 추가

머신러닝 강의 이것도 일부는 들을 필요가 있어 보임. 그래서 이 폴더도 받음.
```bash
git sparse-checkout add MachineLearning
```

#### 2025/3/29 추가

PyTorch 도 받음.
```bash
cd neo-tensorflow2
git sparse-checkout add PyTorch
```
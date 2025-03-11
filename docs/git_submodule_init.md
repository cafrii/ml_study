
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


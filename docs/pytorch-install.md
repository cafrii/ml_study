

# pytorch 설치

https://pytorch.org/

- 2025/3/28 작성

## 채널
오늘 (2025년 3월 28일) 기준으로 확인했을 때, conda 채널에는 pytorch 패키지가 제공되지 않는다. <br>
```
NOTE: Conda packages are no longer available. Please use pip instead.
```
따라서 그냥 맘편하게 pip으로 설치하면 된다.

## 가상환경 문제

~~가상환경 ml_39 를 그대로 사용하도록 한다.~~ <br>
현재 시점으로 pytorch 와 tensorflow 가 동시에 같은 환경에서 설치가 안된다. 충돌하는 의존성은 다음과 같다.
- typing-extensions>=4.10.0 (from torch)
- typing-extensions~=3.7.4 (from tensorflow)

그 결과, 기존에 tensorflow가 설치된 상태에서 pytorch를 설치하려고 하면, 설치는 되긴 하지만 다음과 같이 일부 의존성 패키지가 업데이트가 되면서 tensorflow 동작에 ~~영향을 주게 된다.~~ (확실한 건 아니니) 영향을 줄 가능성이 있다.
```
Successfully uninstalled typing-extensions-3.7.4.3

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
```

**결론 (해결책)**:
- torch 용 가상 환경을 기존에 쓰던것과 분리하여 새로 준비한다.
  - ml_39: conda 채널에서 tensorflow 설치
  - ml_macos: pip으로 mac 전용 패키지 설치
  - ml_torch: pytorch 환경 (pip으로 설치)

이렇게 한 후, 앞으로 pytorch를 사용할 경우에는 `ml_torch` 환경으로 변경하기만 하면 된다.


## 설치 순서 (pytorch)

가상환경
```bash
#---
# 가상환경 생성
conda create -n ml_torch python=3.9
conda activate ml_torch

# 이후 작업은 모두 (ml_torch) 가상환경 내에서 이루어짐.
```

패키지
```bash
# pip으로 패키지 설치
pip3 install torch torchvision torchaudio
```

설치 확인
```bash
python3 -c 'import torch; print(torch.__version__)'
2.6.0
```

### vscode 연동
바로 vscode 에서 쓸 수는 없고 몇 가지 추가 작업이 필요.
- Python 확장을 설치하면 시스템에 설치된 모든 Python 환경(Python 인터프리터와 Python 패키지에 대한 연관된 ​​위치를 의미)을 Python 코드를 실행하는 커널로 사용할 수 있습니다.
- Python 확장을 설치하지 않으면 Jupyter 확장은 Jupyter에 등록된 위치에 설치된 커널 만 찾을 수 있습니다.
- Python의 기본 커널은 IPyKernel 패키지 에서 제공합니다.
- IPyKernel이 설치되지 않은 시스템의 환경을 선택하고 노트북을 실행하려고 하면 IPyKernel을 설치하라는 메시지가 표시됩니다.
- 설치된 경우 해당 환경을 Visual Studio Code에서 Jupyter 노트북의 유효한 커널로 사용할 수 있습니다.
- 참고
  - 사용하려는 Python 환경에 jupyter를 설치할 필요는 없습니다.
  - Python 프로세스를 커널로 시작하고 노트북에 대한 코드를 실행하려면 IPython 과 IPyKernel 만 필요합니다.
    - (예: pip install ipython ipykernel).
  - 자세한 내용은 위키를 방문하세요.
-
- 출처: https://github.com/microsoft/vscode-jupyter/wiki/Jupyter-Kernels-and-the-Jupyter-Extension#python-extension-and-ipykernel

### 그 외 패키지들
```bash
# 주피터 노트북에서 pytorch 사용하기 위한 작업
#conda install -c conda-forge ipykernel
conda install ipykernel

# conda install ipykernel --update-deps --force-reinstall
# 위 명령은 ai에서 알려준 것인데, 참고용으로 남겨둠.
```

위 설치가 제대로 안된 경우에는 노트북에서 cell 실행시 다음과 같이 에러 발생.

> 'ml_torch (Python 3.9.21)'(으)로 셀을 실행하려면 ipykernel 패키지가 필요합니다.
> 다음 명령어를 실행하여 Python 환경에 'ipykernel'을(를) 설치합니다.
>  명령: 'conda install -n ml_torch ipykernel --update-deps --force-reinstall'

끝

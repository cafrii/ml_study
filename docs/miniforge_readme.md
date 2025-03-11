
# Miniforge

이 리포지토리에는 다음과 같은 기능이 미리 구성되어 있는 conda-forge 에 특화된 conda 및 mamba 용 최소 설치 프로그램이 포함되어 있습니다:

- `base` 환경의 패키지는 conda-forge 채널에서 가져옵니다.
- conda-forge 채널은 디폴트 (그리고 유일한) 채널로 설정되어 있습니다.

다양한 CPU 아키텍처 (x86_64, ppc64le, aarch64 (애플 실리콘 포함)) 를 지원하는 데 중점을 두고 있습니다.

🚨PyPy 지원 중단(2024년 8월부터 중단됨) 🚨 지원 중단됨
생략


## 🚨 Mambaforge (Deprecated as of July 2024)

### 2024년 7월 업데이트:

2024년 7월부터 Mambaforge 는 더 이상 사용되지 않습니다. 사용자는 즉시 미니포지3로 전환하시기 바랍니다. 이 설치 프로그램은 2025년 1월 이후 새 릴리스에서 지원되지 않습니다. 마이그레이션을 지원하기 위해 최신 Mambaforge 인스톨러에 롤링 브라운아웃을 도입할 예정입니다. 24.5.0-1 버전까지의 설치 프로그램에는 브라운아웃이 발생하지 않습니다. 24.5.0-1 버전에는 경고 메시지가 포함됩니다. 2024.5.0-2 이상 설치자는 다음과 같은 브라운아웃 일정이 적용됩니다:

- 10월에는 2주마다 설치 프로그램이 진행을 거부합니다.
- 11월에는 10일마다 설치 관리자가 진행을 거부합니다.
- 12월에 5일마다 설치 관리자가 진행을 거부합니다.
- 2025년 이후에는 설치 프로그램이 진행을 거부합니다.

### 이전 정보:

277의 변경 사항이 포함된 Miniforge3-23.3.1-0이 출시됨에 따라 이제 Mambaforge 와 Miniforge3 의 패키지와 구성이 동일해졌습니다. 둘 사이의 유일한 차이점은 설치 프로그램의 이름과 기본 설치 디렉터리뿐입니다.

즉시 미니포지3로 전환하실 것을 권장합니다. 이 설치 프로그램은 2025년 1월에 종료됩니다. CI 사용자의 Miniforge3로의 마이그레이션을 지원하기 위해 최신 Mambaforge (24.5 이상) 설치 프로그램을 다음 일정에 따라 중단합니다.

- 10월 2주마다
- 11월 10일마다
- 12월에는 5일마다
- 2025년 이후에는 없음

24.9.2 릴리스에서 여전히 최신 설치 프로그램을 찾을 수 있습니다.

<br>

# 사용법

미니포지는 콘다와 맘바 명령어를 위한 인스톨러를 제공합니다. OS와 아키텍처에 맞는 설치 프로그램이 실행되면 터미널에서 이 명령어를 사용할 수 있습니다.

## 모든 터미널에서 콘다/맘바 사용 가능

그러나 Windows 설치 프로그램의 디폴트 선택 사항에서는 이러한 명령을 "Anaconda 프롬프트" 에서만 사용할 수 있습니다. 다른 터미널에서 이러한 명령을 사용하려면 Anaconda 프롬프트에서 실행하여 셸에 대한 conda 를 초기화해야 합니다.
```
conda init
```
경로 환경 변수에 `C:\사용자\내사용자명\miniforge3\condabin` 폴더를 수동으로 추가하면 소프트웨어 충돌 가능성이 적은 모든 명령 프롬프트에서 conda 와 mamba 를 더 편리하게 사용할 수 있습니다.

비대화형 설치를 사용하는 경우 유닉스에서도 동일한 상황이 발생합니다. 초기화는 다음과 같이 전체 경로를 사용하여 conda 를 호출하여 수행할 수 있습니다.
```
~/miniforge3/bin/conda init
```


## 환경 자동 활성화

기본적으로, 여러분의 셸에 대해 콘다가 초기화되면, 기본 환경 (`base` environment) 이 활성화되어, 명령 `python` 은 미니포지에서 제공하는 base 파이썬으로 대응이 됩니다. 그리고 `conda install` 은 base 환경에 패키지를 설치하도록 합니다. 이는 편리할 수는 있지만, 이 자동 활성화를 비활성화하는 것이 더 깔끔합니다.
```
conda config --set auto_activate_base false
```
그리고 conda 나 mamba 를 사용하여 다른 환경을 만들고 활성화할 수 있습니다. (예: my_project라는 환경을 만들려면).

```
conda create --name my_project jupyterlab numpy pandas
conda activate my_project
# Now you can start jupyter lab
jupyter lab
```
마지막으로 셸 구성 파일 (일반적으로 Unix의 경우 ~/.bashrc 또는 ~/.zshrc, 윈도우에서라면 notepad $PROFILE 로 편집) 에 활성화 명령을 추가하는 방법도 있습니다.

<br>

# 요구 사항 및 설치 프로그램

기본 환경에서 Python 3.12(*) 최신 인스톨러가 필요합니다:

| OS | Architecture | Minimum Version | File |
| --- | --- | --- | --- |
| Linux	| x86_64 (amd64) | glibc >= 2.17 | Miniforge3-Linux-x86_64.sh |
| Linux	| aarch64 (arm64) (**) | glibc >= 2.17 | Miniforge3-Linux-aarch64.sh |
| Linux	| ppc64le (POWER8/9) | glibc >= 2.17 | Miniforge3-Linux-ppc64le.sh |
| macOS	| x86_64 | macOS >= 10.13 | Miniforge3-MacOSX-x86_64.sh |
| macOS	| arm64 (Apple Silicon) (***) | macOS >= 11.0 | Miniforge3-MacOSX-arm64.sh |
| Windows | x86_64 | Windows >= 7 | Miniforge3-Windows-x86_64.exe |

(*) Python 버전은 base 환경에만 적용됩니다. Conda 는 다양한 Python 버전과 구현으로 새로운 환경을 만들 수 있습니다.

(**) 64비트 프로세서가 포함된 라즈베리파이의 경우, 라즈베리파이 OS 64비트 또는 라즈베리파이용 우분투와 같은 64비트 운영체제도 사용해야 합니다. "시스템: 32비트" 로 표시된 버전은 이 웹사이트의 인스톨러와 호환되지 않습니다.

(***) Apple 실리콘 빌드는 실험 단계이며 다른 플랫폼처럼 테스트가 완료되지 않았습니다.

<br>

# 설치 (인스톨)

...

## 유닉스 계열 플랫폼(macOS, Linux 및 WSL)

터미널 창에서 curl 또는 wget 또는 자주 사용하는 프로그램을 사용하여 컴퓨터의 아키텍처에 적합한 설치 프로그램을 다운로드합니다.

예를 들어
```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```
또는
```
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```

스크립트를 실행합니다.
```
bash Miniforge3-$(uname)-$(uname -m).sh
```

대화형 설치 시 셸에서 conda 를 초기화하라는 메시지가 표시됩니다. 이는 일반적으로 권장되는 워크플로입니다.

비대화형 설치 (예: CI) 의 경우, 다음 명령을 사용할 수 있습니다. (추가 옵션을 나열하려면 `-h` 로 호출):
```
bash Miniforge3-$(uname)-$(uname -m).sh -b
```
대화형 설치가 아닌 경우, 콘다 초기화 명령은 기본적으로 실행되지 않습니다.

macOS에서 미니포지는 홈브루를 통해서도 설치할 수 있습니다.


## CI 파이프라인의 일부로

보다 자동화된 방식으로 명령줄을 통해 적절한 설치 관리자를 다운로드하려면 다음과 유사한 명령을 사용할 수 있습니다.

Linux, 모든 아키텍처의 경우 다음 명령을 사용합니다.
```
wget -O Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```
macOS, 모든 아키텍처의 경우 다음 명령을 사용합니다.
```
curl -fsSLo Miniforge3.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-$(uname -m).sh"
```
그러면 현재 아키텍처에 적합한 설치 프로그램이 Miniforge3.sh 라는 파일명으로 다운로드됩니다. 배치 모드에서 -b 플래시와 함께 명령어로 셸 스크립트를 실행합니다:
```
bash Miniforge3.sh -b -p "${HOME}/conda"
```
-p는 프리픽스 옵션입니다. "${HOME}/conda" 에 디렉토리가 생성됩니다.

그런 다음 콘다 경로를 만들고 콘다를 활성화해야 합니다. 이 명령을 실행합니다:
```
source "${HOME}/conda/etc/profile.d/conda.sh"
# For mamba support also run the following command
source "${HOME}/conda/etc/profile.d/mamba.sh"
```

마지막으로 다음 명령을 실행하여 base 환경을 활성화할 수 있습니다.
```
conda activate
```

<br>

# 언인스톨

중간 생략

## 유닉스 계열 플랫폼(macOS 및 Linux)

미니포지를 제거한다는 것은 설치 과정에서 생성된 파일을 제거하는 것을 의미합니다. 일반적으로 제거해야 할 파일은 다음과 같습니다:

1. 미니포지에 의해 수정된 셸 RC 파일에 대한 모든 수정 사항:

```
# Use this first command to see what rc files will be updated
conda init --reverse --dry-run
# Use this next command to take action on the rc files listed above
conda init --reverse
# Temporarily IGNORE the shell message
#       'For changes to take effect, close and re-open your current shell.',
# and CLOSE THE SHELL ONLY AFTER the 3rd step below is completed.
```

2. 미니포지의 기본 환경이 설치된 폴더와 모든 하위 폴더를 제거합니다:
```
CONDA_BASE_ENVIRONMENT=$(conda info --base)
echo The next command will delete all files in ${CONDA_BASE_ENVIRONMENT}
# Warning, the rm command below is irreversible!
# check the output of the echo command above
# To make sure you are deleting the correct directory
rm -rf ${CONDA_BASE_ENVIRONMENT}
```
3. 남겨진 모든 글로벌 콘다 구성 파일.
```
echo ${HOME}/.condarc will be removed if it exists
rm -f "${HOME}/.condarc"
echo ${HOME}/.conda and underlying files will be removed if they exist.
rm -fr ${HOME}/.conda
```

<br>

# 특징

생략


# 테스트

CI 에서 빌드한 후 인스톨러는 인스톨러 아키텍처($ARCH)와 일치하는 다양한 배포에 대해 테스트됩니다. 예를 들어 아키텍처가 aarch64 인 경우, 빌드된 인스톨러가 테스트 대상입니다:

- Centos 7
- Debian Bullseye (11)
- Debian Bookworm (12)
- Ubuntu 16.04 (LTS)
- Ubuntu 18.04 (LTS)
- Ubuntu 20.04 (LTS)
- Ubuntu 22.04 (LTS)
- Ubuntu 24.04 (Latest release -- also happens to be LTS)

<br>

# 미니포지 인스톨러 빌드

인스톨러는 CI 를 통해 빌드 및 업로드되지만, 직접 Miniforge 인스톨러를 빌드하고 싶다면 다음과 같은 방법을 따르세요:

```
# Configuration
export ARCH=aarch64
export DOCKERIMAGE=condaforge/linux-anvil-aarch64

bash build_miniforge.sh
```

<br>

# 구형 운영 체제 지원

macOS 10.9-10.12 지원
- macOS 10.9~10.12에 대한 지원이 필요한 경우 다음에서 미니포지 24.3.0-0 버전을 다운로드할 수 있습니다.
- https://github.com/conda-forge/miniforge/releases/tag/24.3.0-0

glibc 2.12-2.16 지원
- glibc 2.12~2.16에 대한 지원이 필요한 경우 다음 링크에서 미니포지 24.3.0-0 버전을 다운로드할 수 있습니다.
- https://github.com/conda-forge/miniforge/releases/tag/24.3.0-0


<br>

# FAQ

## 맘바포지와 미니포지의 차이점은 무엇인가요?
2023년 8월 Miniforge 23.3.1 버전이 출시된 이후 Miniforge와 Mambaforge는 본질적으로 동일합니다. 유일한 차이점은 인스톨러의 이름과 기본 설치 경로입니다.

이 릴리스 이전에는 미니포지는 conda 만 제공했지만, 맘바포지는 그 위에 mamba 를 추가했습니다. 미니콘다가 2023년 7월에 conda-libmamba-solver 를 포함하기 시작하자, 미니포지도 8월부터 이를 따라 출시하기 시작했습니다. 그 당시 conda-libmamba-solver 는 libmambapy 에 의존하기 때문에, 미니포지와 맘바포지의 유일한 차이점은 mamba 파이썬 패키지의 존재 여부였습니다. 놀라움을 최소화하기 위해 미니포지에도 mamba 를 추가하기로 결정했습니다.

## 앞으로 둘 중 하나가 더 이상 사용되지 않을 위험을 감수하고 둘 중 하나를 선택해야 하나요?
2024년 6월부로 Mambaforge 는 더 이상 사용되지 않으며, 2025년 1월에 종료될 예정입니다. 사용자는 즉시 미니포지3 로 전환할 것을 권장합니다. 자세한 내용은 위의 참고 사항을 참조하세요.

<br>

# 릴리즈

미니포지의 새 버전을 릴리스하려면:

- GitHub에 $CONDA_VERSION-$BUILD_NUMBER라는 이름의 새 프리 릴리스를 만듭니다.

- CI가 모든 아티팩트를 업로드할 때까지 기다립니다.
  - 각 빌드마다 3개의 아티팩트를 업로드합니다.
    - 버전 이름이 있는 인스톨러 1개
    - 버전 이름이 없는 인스톨러 1개
    - SHA256
  - 이 글을 쓰는 시점에서 72개의 아티팩트를 합한 것이며, 두 개의 소스를 포함하면 총 74개의 아티팩트가 될 것으로 예상됩니다.

- 프리 릴리스를 릴리스로 표시합니다.

참고: 사전 릴리스를 사용하면 최신 링크가 작동하는지 확인하는 것이 중요합니다.



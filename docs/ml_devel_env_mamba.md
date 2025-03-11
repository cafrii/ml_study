
## Mamba 는 Miniforge 에 흡수됨!

결론 부터 먼저 말하면..
- MambaForge 라는 이름의 설치 프로그램은 더 이상 쓰지 않아야 한다.
- 그냥 최신 MiniForge 를 설치하면 그 안에 mamba 가 있다.


아래 Miniforge 발췌 참고: (https://github.com/conda-forge/miniforge)
>
> 2024년 7월부터 Mambaforge 는 더 이상 사용되지 않습니다. 사용자는 즉시 미니포지3로 전환하시기 바랍니다. 이 설치 프로그램은 2025년 1월 이후 새 릴리스에서 지원되지 않습니다.
>

<br>
아래 내용 중 MambaForge 관련 내용은 이미 예전 내용이니 감안 해서 볼 것!

<br>


## MiniForge 설치

예전에는 별도의 mambaforge 배포가 따로 있었던 것 같은데.. 지금은 miniforge 를 설치하면 그 안에 mamba 가 포함되어 있는 것으로 보인다.

(정확하진 않으나, 대체로 miniforge 23.3.1 이후 버전이라면 괜찮은 모양임)

새로 시작할 거라면 그냥 최신 버전, 또는 직전 메이저 안정 버전을 사용하도록 한다.

2025/3/11 기준, Miniforge 최신은 24.11.3-0 이다. 연도와 날짜로 보임.
https://github.com/conda-forge/miniforge/releases/tag/24.11.3-0

직접 다운로드 링크: <br>
https://github.com/conda-forge/miniforge/releases/download/24.11.3-0/Miniforge3-24.11.3-0-MacOSX-arm64.sh


```
mkdir -p miniforge3/24.11.3-0
cd miniforge3/24.11.3-0

curl -L -O https://github.com/conda-forge/miniforge/releases/download/24.11.3-0/Miniforge3-24.11.3-0-MacOSX-arm64.sh

bash Miniforge3-24.11.3-0-MacOSX-arm64.sh
```

주의:
- 설치 후 Anaconda default 채널이 구성되어 있지 않아야 함.
- 설치가 문제 될 수 있으므로 base 환경에 아무것도 설치하지 않아야 함.

위 두번째 주의 사항이 중요하다. 설치 할 때 옵션에 따라 자동 활성화가 켜져 있을 수도 있다.
혹시, 쉘 실행 시 자동으로 (base) 환경이 활성화 된다면 (프롬프트에 `(base)` 라고 표시됨) 이는 별로 바람직한 것은 아니므로 아래 명령을 실행하여 자동 활성화를 끄는 것이 좋다.
```
conda config --set auto_activate_base false
```


<br><br>
-------
아래 내용은 참고용이다.
<br>

## Mamba 는 또 무엇인가?

Mamba 는 또 MiniForge 에서 패키지 매니저 프로그램이 conda 대신 mamba 로 대체된 거라고 한다.

Mamba가 기본 패키지 매니저로 설정된 Miniforge 를 Mambaforge 라도 부르는 것 같음.

속도가 (훨씬?) 더 빠르다고 하는데, 여기서의 속도는 파이썬 패키지의 실행을 말하는 게 아니라 패키지 관리자의 속도가 빠르다는 말로 이해된다.

그렇다면 결론은, 그냥 Mamba 를 쓰면 될 것 으로 보이는데..


심지어, Mamba 를 설치하면 그 안에 conda 패키지 관리자도 포함되어 있다고 함. 그래서, 때에 따라 골라가며 실행할 수 있다!!

참고: 기본 설치 경로는 miniforge 와 mambaforge 가 다르니까, 그것만 주의하면 된다.

굳이 miniforge 설치하고 mambaforge 또 설치하고, 이렇게 하지 말자! 디스크만 괜히 낭비할 수도 있다.

```
source ~/mambaforge/bin/activate

# conda 명령어 사용 가능
conda create -n test_env python=3.10
conda activate test_env
conda install numpy

# 같은 환경에서 mamba 사용 가능
mamba install pandas
mamba update --all  # 더 빠르게 패키지 업데이트
```

결론
- Mambaforge에서 conda와 mamba를 같이 사용하면 됨!
- 따라서 Miniforge를 따로 설치할 필요 없음!
- 디스크 낭비 없이, 필요할 때 빠른 mamba를 쓰고, 기존 conda 명령어도 그대로 사용 가능!
- 즉, Miniforge 대신 Mambaforge 하나만 설치하면 됨.


<br>

## 기존 miniconda3 설치 완전 제거하기

오래 전에 설치한 miniconda3 는 더 이상 쓸 일은 없을 것이므로, 완전히 삭제한다.

```
# 폴더 제거
rm -rf ~/miniconda3

# zsh 통합 코드 제거
vi ~/.zshrc
# >>> conda initialize >>>
...
# <<< conda initialize <<<
위 영역에 해당되는 라인 제거

source ~/.zshrc

# PATH 에서 miniconda3/ 관련 부분 제거. 그냥 shell 을 다시 실행하는 것도 좋음.

# 캐시 정리
rm -rf ~/.conda ~/.continuum

# rc 정리
rm -f ~/.condarc
```
<br>


## Mamba 정보

2025.3.11 업데이트

GitHub: <br>
https://github.com/mamba-org/mamba

설치 가이드: <br>
https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html

Miniforge 릴리즈: <br>
https://github.com/conda-forge/miniforge/releases


<br>



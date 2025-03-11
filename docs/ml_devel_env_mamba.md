

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
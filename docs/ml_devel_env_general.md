
# ML 개발 환경 설치 관련 내용 정리


## pip vs. conda

일단 무조건 가상환경은 필수라고 보고, pip 의 venv 와 conda 와의 비교라고 볼 수 있다.

**결론: conda 가 추천됨. conda 관련 질문은 아래에서.**

채널에 대해서: <br>
pip 의 경우 PyPI (Python Package Index) 라는 곳에서 패키지를 내려 받는다.
반면 conda 의 경우 여러 곳에서 받을 수 있는데 각각을 채널이라고 부름.

결국 채널이란 패키지가 저장되어 있고 호스팅되는 위치를 말함.
PyPI 를 채널이라고 부르지는 않음.


## Anaconda vs. Miniforge

Anaconda 가 너무 무거워서, 빌트인 패키지를 제거한 채로 배포되는 Miniconda 가 생겨나고,
기본 anaconda 채널 외에 conda-forge 채널을 사용하는 "forge" 류의 콘다도 출현한게 아닐까 생각된다.

Conda 의 Anaconda vs Miniforge 비교 (Chat-GPT)

| 특징 | Anaconda | Miniforge |
| --- | --- | --- |
| 기본 패키지 포함 여부	| 많은 패키지가 기본 포함됨 | 최소한의 패키지만 포함 |
| 용량 | 수 GB | 수백 MB |
| Conda 배포판 | 공식 Anaconda 채널 | Conda-Forge 채널 기반 |
| Python 기본 버전 | 포함됨 | 포함되지 않음 |
| 설치 방식	| GUI 또는 CLI | CLI 설치 |

추천:
- 본인의 경우는 miniforge 가 딱 맞는다.

Miniforge 를 선택해야 하는 또 다른 중요한 이유: <br>
- 미니포지는 `conda-forge` 라는 커뮤니티 기반의 패키지 저장소를 기본 채널로 사용한다. 이곳은 애플실리콘 M1/M2 등을 위한 ARM64 아키텍처 전용 빌드를 제공한다.
- 아나콘다의 디폴트 채널도 일부 제공하고 있으나 아직 부족하며, x86_64 용 패키지라면 로제타 변환을 거쳐 실행되어야 하니 성능 상으로도 안좋다.



## 패키지 저장 위치

생성되고 activate 된 후 설치된 패키지는 아래 위치에 저장된다. 이는 각 사용자 별 고유한 위치이므로, 같은 이름이라면 가상환경을 공유하게 된다.

이는 venv 모듈을 이용한 방식과 다르니 주의가 필요하다.

```
~/miniforge3/envs/<가상환경이름>/
```

아래와 같이 커스텀 경로를 사용할 수도 있다고 함. 이 방법을 사용하면 동일한 이름의 가상 환경을 여럿 만들 수도 있을 것 같음.
```bash
conda create -p /path/to/env python=<version>
```

## conda 와 pip 패키지 이름

이름은 대체로 동일하다고 보면 된다.
- numpy, pandas, tensorflow, ...

이는 어떠한 규정이 있기 때문은 아닌거 같고, 대부분의 패키지 개발자들이 관례적으로 그렇게 하는 것으로 보인다. 혼란을 줄이고 일관성을 유지하기 위해서는 당연하다고 봄.

하지만, 일부 패키지는 이름이 서로 다르거나,
- opencv-python (pip) vs. opencv (conda)

일부 패키지는 한 군데 에서만 존재한다.
- tensorflow-metal 은 pip 에만 있음.

특히 마지막 경우라면, 결국 두 종류의 패키지를 다 사용할 수 밖에 없을 것으로 보인다.


## conda 패키지와 pip 패키지 충돌

conda 가상환경에서도 pip 패키지 설치가 가능하다. 다음과 같이 pip 을 먼저 설치하면 된다.
```bash
conda install pip
pip install <pip_package>
```

하지만, 동일 가상환경 내에서 conda 패키지와 pip 패키지를 둘 다 설치 할 경우 충돌 문제가 발생할 수 있다.

```bash
conda install numpy  # conda 버전 numpy 설치
pip install numpy  # pip 버전 numpy 설치
```

이 경우, pip 버전 패키지가 conda 버전을 **덮어쓸 수도** 있다고 한다.

"덮어쓸 수도 있음" 과 같이 가능성으로만 표현한 것은, 그럴 수도 아닐 수도 있다는 것 처럼 들리는데, 어쨌든 이러한 상황은 만들지 말아야 한다.

추천되는 방법: <br>
가급적 conda 패키지를 먼저 설치한 후, 없으면 pip 패키지 이용.

팁: <br>
`conda search <package>` 또는 -`pip search <package>`-- 로 검색을 해 보아야 함.--

// 마크다운에서 취소선을 표시하려면?

주의: `pip search` 는 더 이상 지원하지 않아 보임. 브라우저에서 `https://pypi.org/search` 를 이용해야 함.


주의: <br>
절대로 `pip install --upgrade <...>` 는 하지 말아야 한다. 설치 된 conda 패키지를 망가뜨릴 수 있다!





## 텐서플로 패키지 설치

### 가상 환경 준비

먼저 conda 가상 환경을 활성화 한다. 아직 생성하지 않았다면 생성 부터 한다. python 3.9 가 제일 안정적이라고 한다.

하지만 일단 가상환경이 생성된 이후에 python 버전을 업그레이드 하는 것은 여러모로 추천되지 않으며, 새롭게 가상환경을 생성하는 것이 권장된다. 그래서 아예 처음부터 가상환경 이름에 파이썬 버전 정보를 포함하도록 한다.

아래 예시는 python 3.9 를 사용하는 `ml_39` 이라는 이름의 가상환경을 생성하고 활성화 하고 있다.
```bash
conda create -n ml_39 python=3.9

conda env list

conda activate ml_39

(ml_39) ...
```

참고로, (2025/3 기준으로) 현재 ml_39, ml_macos 이렇게 두 종류의 가상 환경을 설치해서 사용 중이다. macos 전용 가상환경에 대해서는 뒤에서 설명한다.


### 설치할 패키지

tensorflow 라는 패키지 하나만 설치하면 된다. 나머지는 의존성에 따라 알아서 설치된다. 고려해야 할 부분은, Apple 에서 따로 최적화한 버전을 선택 할 것인지 여부이다.

Apple 에서 직접 관리하는 다음 두 가지 패키지 이다.
- tensorflow-macos
- tensorflow-metal

tensorflow-macos 는 CPU 전용, tensorflow-metal 은 GPU 가속 지원 버전이다.
하지만, tensorflow-metal 단독으로는 동작하지 않는다. 따라서 위 두 패키지를 모두 설치해야 한다.

하지만 이 macos 용 tensorflow는 버전이 최신이 아니며, 특히 PyLint 관련한 몇 가지 버그(?)가 수정 반영이 안되어서, 코드 작성 및 분석에 매우 불편함이 따른다.

그래서, 두 종류의 가상환경을 모두 설치해 두고, 번갈아 가면서 사용하는 방법을 사용한다.
- ml_39 (또는 ml_310): 일반 작업에 사용. 코드 작성, 분석, 디버깅 등.
- ml_macos: mac os 용 GPU 가속이 필요한 경우에 사용.



!! 주의 !!
- 애플이 배포하는 패키지는 conda 채널이 아닌 PyPI 에서 제공한다. 따라서 pip 으로 설치해야 한다. 즉, conda 가성환경 안에서 pip 패키지를 설치하는 것이다. 일반 tensorflow 패키지는 conda-forge 채널에서 제공하는 것이 더 최신이다.

!! 주의 !!
- tensorflow-macos 와 tensorflow 패키지를 한 가상환경 안에 같이 설치하면 안된다!


### PIP 설치

pip 이 필요하므로 pip 을 설치해야 한다.
conda 채널의 pip 버전이 낮을 수 있으니 pip 을 업그레이드 한다. (하지만 확인 결과 최신 miniforge3 설치에 포함된 base 가상환경의 pip 버전은 충분히 높아서 따로 업그레이드가 필요하진 않았다.)

```bash
# 버전 확인
pip --version
pip 25.0.1 from ...miniforge3/envs/ml/lib/python3.9/site-packages/pip (python 3.9)

# 설치
python -m pip install --upgrade pip
```

### 패키지 설치

앞서 설명한 대로 텐서플로 패키지를 설치한다.
```bash
conda activate ml_39
(ml_39)
conda install tensorflow

conda activate ml_macos
(ml_macos)
pip install tensorflow-macos tensorflow-metal
```

### 확인

동작을 확인한다. (이 코드에서부터는 activate 명령은 따로 기술하지 않았음)
```
(ml_39)
python -c "import tensorflow as tf; print(tf.config.experimental.list_physical_devices('GPU'))"

결과
[]

(ml_macos)
python -c "import tensorflow as tf; print(tf.config.experimental.list_physical_devices('GPU'))"

결과
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

ml_macos 환경에서는 GPU 정보가 표시되어야 정상이다.


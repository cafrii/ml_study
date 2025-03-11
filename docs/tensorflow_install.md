

## 텐서플로 패키지 설치

### 가상 환경 준비

먼저 conda 가상 환경을 활성화 한다. 아직 생성하지 않았다면 생성 부터 한다. python 3.9 가 제일 안정적이라고 한다. 아래 예시는 `ml` 이라는 이름의 가상환경임.
```
conda create -n ml python=3.9

conda activate ml
```

### 패키지 정보

설치해야 하는 패키지는 Apple 에서 직접 관리하는 다음 두 가지 패키지 이다.
- tensorflow-macos
- tensorflow-metal

tensorflow-macos 는 CPU 전용, tensorflow-metal 은 GPU 가속 지원 버전이다.
하지만, tensorflow-metal 단독으로는 동작하지 않는다. 따라서 위 두 패키지를 모두 설치해야 한다.

!! 주의 !!
- 위 패키지는 conda 채널이 아닌 PyPI 에서 제공한다. 따라서 pip 으로 설치해야 한다.
즉, conda 가성환경 안에서 pip 패키지를 설치하는 것이다.

!! 주의 !!
- tensorflow 패키지는 설치하지 않아야 한다.

### PIP 설치

pip 이 필요하므로 pip 을 설치해야 한다.
conda 채널의 pip 버전이 낮을 수 있으니 pip 을 업그레이드 한다.

```
# 버전 확인
pip --version
pip 25.0.1 from ...miniforge3/envs/ml/lib/python3.9/site-packages/pip (python 3.9)

# 설치
python -m pip install --upgrade pip
```

### 패키지 설치

그리고 나서 패키지를 설치한다.
```
pip install tensorflow-macos tensorflow-metal
```

### 확인

동작을 확인한다.
```
python -c "import tensorflow as tf; print(tf.config.experimental.list_physical_devices('GPU'))"

[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

GPU 정보가 표시되면 OK.

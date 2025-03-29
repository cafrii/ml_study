
# ML 개발 환경 내 패키지 설치 내용

기본적인 ml_39 가상환경에 설치한 것을 기준으로 정리한다.


## tensorflow
// for ml_39: <br>
conda install tensorflow

// for ml_macos, ml_torch: <br>
pip install tensorflow-macos tensorflow-metal

## ipykernel
conda install ipykernel

// for ml_macos: <br>
pip install ipykernel

## google
pip install google-colab
<br>-> 실패

## matplotlib
// for ml_39
conda install matplotlib
<br> -> 일부 패키지들은 다운그레이드 됨.
2025/3/13

```
matplotlib       3.9.4   py39hdf13c20_0   conda-forge
matplotlib-base  3.9.4   py39h7251d6c_0   conda-forge
```
matplotlib-inline 는 원래 설치되어 있었음.

// for ml_macos, ml_torch: <br>
pip install matplotlib


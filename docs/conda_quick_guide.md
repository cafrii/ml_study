


## Conda 명령어 Quick Guide

### 가상 환경 생성 및 활성화/비활성화
```
conda create -n myenv python=3.9
conda activate myenv

(myenv)
..

conda deactivate
```

### 생성되어 있는 가상환경 목록
```
conda env list
  ..
  base                   /Users/yhlee/miniforge3
  ml                     /Users/yhlee/miniforge3/envs/ml

conda info --env
```

### 패키지 목록
```
conda list
conda export
```

### 패키지 설치
```
conda install <패키지이름>
```

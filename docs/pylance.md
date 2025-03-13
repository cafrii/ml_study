

## 파이선 코드에서 물결선 과 함께 분석이 안되는 문제

### 원인

pylance 가 가상환경 모듈 폴더를 인식 못함.
아래 설정 없이도 잘 되는 경우도 있긴 하던데, 언제 되고 언제 안되는지 명확하지 않음.

### 해결

vs code 설정 -> python analysis 로 검색.

수정 적용 범위를 '작업 영역' 으로 선택하고

**Python > Analysis: Extra Paths**<br>
추가 가져오기 검색 확인 경로<br>
'항목 추가' 버튼을 누르고 아래 입력.
```
~/miniforge3/envs/ml/lib/python3.9/site-packages
```

또는,

현재 프로젝트 (폴더) 에 `.vscode/settings.json` 파일이 있다면, 아래 내용을 추가. UI 설정과 동일한 것임.

```
{
    "python.analysis.extraPaths": [
        "~/miniforge3/envs/ml_39/lib/python3.9/site-packages"
    ]
}
```

상대 경로 및 ~ 도 잘 인식하지, 굳이 어렵게 절대 경로를 쓰려고 노력하지 않아도 됨.
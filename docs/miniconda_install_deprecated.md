

## 경고
2025/3/11

Miniconda 보다는 MiniForge 를, MiniForge 보다는 MambaForge 가 추천된다.

이 문서는 그냥 참고용으로만 유지되고 있을 뿐이므로 다른 MambaForge 관련 문서를 참고하는 것이 좋다.


<br><br>


## 설치 여부 확인

이미 설치가 되어 있을 수도 있다. 확인을 먼저 하는 것이 좋다.

아마도 ~/miniconda3/ 폴더에 설치되어 있을 확률이 높으니 이 폴더 유무를 확인해 본다.

또한, 경로 PATH 도 확인해 본다.
```bash
echo $PATH | grep conda
...:<MyHome>/miniconda3/condabin:...
```

저 폴더에 conda 실행 파일이 존재하므로, 실행하여 버전을 확인해 보면 된다.
```
conda --version
24.5.0
```

## 설치

다운로드 하고 실행하면 된다.
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh

PREFIX="${HOME:-/opt}/miniconda3"

bash ./Miniconda3-latest-MacOSX-arm64.sh -b -u
```

옵션 설명
- `-b`: 배치 모드
- `-u`: 기존 설치가 있을 경우 업데이트


### 결과
~/miniconda3 폴더가 만들어진다.


다음과 같은 내용이 ~/.zshrc 에 삽입된다.
```zsh
...
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/yhlee/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/yhlee/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/yhlee/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/yhlee/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
...
```

끝

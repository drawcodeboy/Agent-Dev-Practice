# Agent Study
에이전트 개발에 필요한 기술 스택 스터디 코드 모음

## Install
```
conda create -n agent_dev python=3.12
conda activate agent_dev
```

## Freq. Note
```
## 환경 추출
conda env export > environment.yml
conda env export --no-builds > environment.yml # 빌드 식별자 X
conda env export --no-builds | sed '/^prefix:/d' > environment.yml # prefix는 다른 환경에 갔을 때 필요 없어서 X

## 환경 생성
conda env create -f environment.yml
```

## Study
1. FastAPI


# DataLoaders 클래스

## pytorch 의 DataLoader
torch 에 DataLoader 라는 클래스가 있다.

> 참고: https://tutorials.pytorch.kr/beginner/basics/data_tutorial.html


torch DataLoader 의 아주 간략한 정의
- ``Dataset`` 은 데이터셋의 특징(feature)을 가져오고 하나의 샘플에 정답(label)을 지정하는 일을 한 번에 합니다.
- 모델을 학습할 때, 일반적으로 샘플들을 "미니배치(minibatch)"로 전달하고, 매 에폭(epoch)마다 데이터를 다시 섞어서 과적합(overfit)을 막고,
- Python의 ``multiprocessing`` 을 사용하여 데이터 검색 속도를 높이려고 합니다.
- ``DataLoader`` 는 간단한 API로 이러한 복잡한 과정들을 추상화한 순회 가능한 객체(iterable)입니다.

> #### ⚠️ 주의:
> Dataset 이름에서 s 가 소문자이다! 반면 DataLoader 에서 L 은 대문자.

내 식으로 풀어본다면,
- Dataset 객체는 실제 데이터를 가지고 있는 객체이다. (그 데이터는 훈련 데이터와 레이블 로 구성되어 있음)
  - 아주 많은 수의 데이터 항목을 가지고 있을 것이다.
- DataLoader 객체는 자신이 담당하는 DataSet 객체를 쉽게 사용할 수 있게 해 주는 유틸리티 객체이다.
  - 한번에 하나씩 열거 할 수 있게 해 준다거나, 순서를 셔플링 해 준다거나..

사용 예:
```python
from torch.utils.data import Dataset, DataLoader

training_data:Dataset = ... # 여러가지 방법으로 데이터셋 확보

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
```

## fastai 의 DataLoader


예시들

```python
dls1 = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=.., splitter=.., get_y=parent_label, item_tfms=..
).dataloaders(path, bs=32)

dls2 = ImageDataLoaders.from_folder(trn_path, seed=42, valid_pct=0.2, item_tfms=item, batch_tfms=batch)

```


# 사용법 요약 비교

vision 관련 ML 모델을 이용한 일반적인 작업 절차들 요약 정리

## 0. 데이터 준비, 전처리

TODO


## 1. DataLoader
맨 먼저 DataLoader 를 준비한다.
보통은 dls 라는 이름을 사용한다.

#### DataBlock 으로부터..
```python
# 예: Is it a bird?
dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=.., splitter=.., get_y=parent_label, item_tfms=..
).dataloaders(path, bs=32)

```

#### ImageDataLoaders 클래스를 이용하여..

```python
# small models
dls = ImageDataLoaders.from_folder(trn_path, seed=42, valid_pct=0.2, item_tfms=item, batch_tfms=batch)
```

- valid_pct
- item_tfms
- batch_tfms
  - aug_transforms(size=128, min_scale=0.75)

#### Pandas DataFrame 으로부터

```python
dls = CollabDataLoaders.from_df(ratings, item_name='title', bs=64)

# 몇 가지 후속 처리까지 같이 수행?
dls = TabularPandas(
    df, splits=splits,
    procs = [Categorify, FillMissing, Normalize],
    cat_names=["Sex","Pclass","Embarked","Deck", "Title"],
    cont_names=['Age', 'SibSp', 'Parch', 'LogFare', 'Alone', 'TicketFreq', 'Family'],
    y_names="Survived", y_block = CategoryBlock(),
).dataloaders(path=".")

```


## 2. 데이터 확인
- dls.show_batch(max_n=3)


## 3. Learner

- vision_learner()
```
# post 예시: Is it a bird?
learn = vision_learner(dls, resnet18, metrics=error_rate)

# first step
learn = vision_learner(dls, 'resnet26d', metrics=error_rate, path='.').to_fp16()

# small models
learn = vision_learner(dls, arch, metrics=error_rate).to_fp16()
```

## 4. Fine tuning

#### 학습률 결정
```
learn.lr_find(suggest_funcs=(valley, slide))
```

#### 미세 조정
```
# first step
learn.fine_tune(3, 0.01)

# small models
learn.fine_tune(epochs, 0.01)

```


## 5. Predict

- vision_leaner
```
# is it a bird?
is_bird,_,probs = learn.predict(PILImage.create('bird.jpg'))
```

```
# first step
probs,_,idxs = learn.get_preds(dl=tst_dl, with_decoded=True)
```


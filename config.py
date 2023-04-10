import os
from dataclasses import dataclass

base = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(base, 'data')
train = os.path.join(data, 'train')
test = os.path.join(data, 'test')
unlabeled = os.path.join(data, 'unlabeled')


@dataclass
class CFG:
    NCOLS: int = 20
    NROWS: int = 100
    BASE_PATH: str = base
    DATA_PATH: str = data
    TRAIN_PATH: str = train
    TEST_PATH: str = test
    UNLABELED_PATH: str = unlabeled
    SAVEFIG: bool = False
    SAVE_PARQUET: bool = True
    SEED: int = 42

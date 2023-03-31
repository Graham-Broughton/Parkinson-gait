import gc
from glob import glob

import pandas as pd
from colorama import Fore, Style
from tqdm import tqdm

red = Style.BRIGHT + Fore.RED
blu = Style.BRIGHT + Fore.BLUE
mgt = Style.BRIGHT + Fore.MAGENTA
grn = Style.BRIGHT + Fore.GREEN
gld = Style.BRIGHT + Fore.YELLOW
res = Style.RESET_ALL


def file_reader(file):
    """
    Reads a filepath to a csv and adds Id from the filepath to the resulting dataframe
    """
    df = pd.read_csv(file)
    df['Id'] = file.split('/')[-1].split('.')[0]
    return df


def concat_to_parquet(CFG, metadata, dataset: str = 'tdcsfog'):
    print(f'\t{grn}Reading {blu}{dataset} {grn}files{res}')
    files = glob(f'{CFG.TRAIN_PATH}/{dataset}/*')

    df = pd.concat([file_reader(file) for file in tqdm(files)])
    print(f'\t{gld}Dataset: {blu}{dataset} {gld}merged shape \t --> \t {red}{df.shape}{res}')

    df = df.merge(metadata, how='inner', on='Id')

    df.to_parquet(f'{CFG.TRAIN_PATH}/{dataset}_merged.parquet.gz', compression='gzip')
    del df, files
    gc.collect()

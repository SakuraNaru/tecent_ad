import pandas as pd
import os

def merge_adfeature():
    xi = 1
    df_adfeature = pd.read_csv('preliminary_contest_data/adFeature.csv')

    while os.path.exists('preliminary_contest_data/cut_train/train_%s.csv' %xi):
        df_train = pd.read_csv('preliminary_contest_data/cut_train/train_%s.csv' %xi)
        df_train = pd.merge(df_train, df_adfeature, how='left', on = 'aid')
        df_train.to_csv('preliminary_contest_data/merge_feature/train%s.csv' %xi, index = False)
        xi = xi + 1

def merge_userfeature():
    xi = 1
    yi = 0
    while os.path.exists('preliminary_contest_data/cut_user/userFeature%s.csv' %yi):
        df_userfeature = pd.read_csv('preliminary_contest_data/cut_user/userFeature%s.csv' %yi)
        while os.path.exists('preliminary_contest_data/merge_feature/train%s.csv' %xi):
            df_train = pd.read_csv('preliminary_contest_data/merge_feature/train%s.csv' %xi)
            df_train = pd.merge(df_train, df_userfeature, how='inner', on = 'uid')
            df_train.to_csv('preliminary_contest_data/merge_feature/train%s.csv' %xi, index = False)
            xi = xi + 1
        yi = yi + 400000

if __name__ =='__main__':
    merge_adfeature()
    merge_userfeature()
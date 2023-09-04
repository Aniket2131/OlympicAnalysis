import pandas as pd


def preprocessor(df,region_df):
    df_summer = df[df['Season'] == 'Summer']
    df_summer = df_summer.merge(region_df, on='NOC', how='left')
    df_summer.drop_duplicates(inplace=True)
    df_summer = pd.concat([df_summer, pd.get_dummies(df_summer['Medal'], dtype='int32')], axis=1)
    return df_summer

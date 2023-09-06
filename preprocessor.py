import pandas as pd


def preprocessor(df, region_df, season):
    new_df = df[df['Season'] == season]
    new_df = new_df.merge(region_df, on='NOC', how='left')
    new_df.drop_duplicates(inplace=True)
    new_df = pd.concat([new_df, pd.get_dummies(new_df['Medal'], dtype='int32')], axis=1)
    return new_df

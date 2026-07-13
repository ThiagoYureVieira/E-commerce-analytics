import pandas as pd


def remove_duplicates(df):
    return df.drop_duplicates()


def remove_extra_spaces(df, columns):
    for column in columns:
        df[column] = df[column].str.strip()
    return df


def convert_to_datetime(df, columns, format):
    for column in columns:
        df[column] = pd.to_datetime(df[column], format=format)
    return df


def fill_null(df, column, value):
    df[column] = df[column].fillna(value)
    return df
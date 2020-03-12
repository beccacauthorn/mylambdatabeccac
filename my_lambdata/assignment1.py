import pandas as pd


def split_date(df, col_name):
    # Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
    aux_col = pd.to_datetime(df[col_name], infer_datetime_format=True)
    
    # Extract components from date_recorded, then drop the original column
    df['year'] = aux_col.dt.year
    df['month'] = aux_col.dt.month
    df['day'] = aux_col.dt.day

    return df


def check_nulls(df):
    #Check a dataframe for nulls, print/report them in a nice "pretty" format
    nulls = df.isnull().sum()

    for row in nulls.iteritems():
      print('The column', row[0], 'has', row[1], 'nulls.')

    return

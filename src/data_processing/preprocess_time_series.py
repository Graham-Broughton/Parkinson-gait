def convert_g_2_msecsqrd(df):
    """
    Converts the accelerometer data in tdcsfog dataset from g to m/s^2
    """
    df['AccV'] = df['AccV'].apply(lambda x: f'{x * 9.80665:.5f}')
    df['AccML'] = df['AccML'].apply(lambda x: f'{x * 9.80665:.5f}')
    df['AccAP'] = df['AccAP'].apply(lambda x: f'{x * 9.80665:.5f}')
    return df

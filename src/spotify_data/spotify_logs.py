import os
import pandas as pd


def read_endsong(trackdone=True):
    data_location = '..\data\endsong_'

    # read first file to get df format
    index = 0
    df = pd.read_json(f'{data_location}{index}.json')
    index += 1

    # append the rest of the files
    while os.path.exists(f'{data_location}{index}.json'):
        df = pd.concat([df, pd.read_json(f'{data_location}{index}.json')])
        index += 1

    if trackdone:
        df = df[df.reason_end == 'trackdone']

    # datetime parse
    df['ts'] = pd.to_datetime(df.ts, utc=True)
    df.ts = df.ts.dt.tz_convert('America/Argentina/Cordoba')

    return df

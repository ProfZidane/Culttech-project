import numpy as np
import pandas as pd



def load_news():
    df = pd.read_csv('./data/culttech_source.csv', header=None, names=['name', 'type', 'url'])    
    print(f"Original size : {len(df)}")
    df = df[df['url'].notna()]
    df['url'] = df['url'].str.replace('feed/', '', regex=False)            
    df = df[df['url'].str.startswith('http')]    
    print(f"Loaded {len(df)} sources from CSV")
    return df.to_dict(orient='records')  # Limiter à 20 pour le test



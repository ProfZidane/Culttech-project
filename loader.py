import numpy as np
import pandas as pd
import feedparser
import requests
from datetime import datetime
from urllib.parse import urlparse
import re
from html import unescape


def is_xml_feed(url):
    try:
        response = requests.head(url, timeout=10)
        content_type = response.headers.get('content-type', '').lower()
        return 'xml' in content_type or 'rss' in content_type or url.endswith('.xml') or 'feed' in url
    except:
        return url.endswith('.xml') or 'rss' in url or 'feed' in url

def clean_html_description(text):
    if not text:
        return ''
    text = re.sub(r'<[^>]+>', '', text)
    text = unescape(text)
    return text.strip()

def parse_rss_feed(url):
    try:
        feed = feedparser.parse(url)
        articles = []
        
        for entry in feed.entries:  
            article = {
                'name': entry.get('title', 'Sans titre'),
                'type': 'ARTICLE',
                'url': entry.get('link', url),
                'description': clean_html_description(entry.get('description', '')),
                'created_at': datetime.now(),
                'source_feed': url
            }
            articles.append(article)
        
        return articles
    except Exception as e:
        print(f"Erreur lors du parsing RSS de {url}: {e}")
        return []

def load_news():
    df = pd.read_csv('./data/culttech_source.csv', header=None, names=['name', 'type', 'url'])    
    print(f"Original size : {len(df)}")
    df = df[df['url'].notna()]
    df['url'] = df['url'].str.replace('feed/', '', regex=False)            
    df = df[df['url'].str.startswith('http')]    
    print(f"Loaded {len(df)} sources from CSV")
    df_limited = df.head(10)
    all_articles = []

    for _, row in df_limited.iterrows():
        url = row['url']
        
        if is_xml_feed(url):
            print(f"Parsing RSS feed: {url}")
            articles = parse_rss_feed(url)
            all_articles.extend(articles)
        else:
            article = {
                'name': row['name'],
                'type': row['type'],
                'url': url,
                'description': '',
                'created_at': datetime.now(),
                'source_feed': None
            }
            all_articles.append(article)
    print(f"Total articles loaded: {len(all_articles)}")
    return all_articles


from constants import *
import pandas as pd
from tqdm import tqdm
from textblob_de import TextBlobDE as TextBlob
import nltk
import joblib
import numpy as np
import multiprocessing
nltk.download('punkt')

df = pd.read_csv(os.path.join(DATA_PATH, "srf_data/processed/processed_new.csv"))
df = df[df.corona_articles.notna()].copy()

def extract_sentiment(row):
    i, data = row
    sentiment = TextBlob(data.corona_articles).sentiment
    return(sentiment.polarity, i, sentiment.subjectivity)

pool = multiprocessing.Pool(6)
sentiments = set()
for row in tqdm(pool.imap_unordered(extract_sentiment, df.iterrows(), chunksize=10), total=len(df)):
    sentiments.add(row)
pool.close()
pool.join()

sentiments = sorted(sentiments)
joblib.dump(sentiments, os.path.join(DATA_PATH, "srf_data/processed/sentiments.joblib"))
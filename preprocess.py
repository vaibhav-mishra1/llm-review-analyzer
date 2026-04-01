import pandas as pd
import numpy as np
import re

df = pd.read_csv("product_reviews.csv", encoding="utf-8")

def clean_text(text):
    if pd.isna(text):
        print("exicuted 1")
        return ""
    
    text = str(text)
    
    text = text.lower()
    
    # Remove emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # Remove special characters (keep words & numbers)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def remove_noise(text):
    if not isinstance(text, str):
        return text
        
    return " ".join([w for w in text.split() if w not in noise_words])

df['cleaned_review'] = df['content'].apply(clean_text)

noise_words = {'pros', 'cons', 'drawback', 'problem'}

df['cleaned_review'] = df['cleaned_review'].apply(remove_noise)

df.to_csv("cleaned_product_reviews.csv", index=False)
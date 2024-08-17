import nltk
import re
import heapq
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Data Preprocessing
def clean_text(text):
    # Remove special characters and digits
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_words = [word for word in word_tokens if word not in stop_words]
    return filtered_words

# Feature Engineering
def rank_sentences(text, word_frequencies):
    sentence_scores = {}
    sentences = sent_tokenize(text)
    
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if len(sentence.split(' ')) < 30:  # Consider only sentences with less than 30 words
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
    
    return sentence_scores

# Summarization
def generate_summary(text, top_n=2):
    clean_article = clean_text(text)
    words = preprocess_text(clean_article)
    
    word_frequencies = nltk.FreqDist(words)
    max_frequency = max(word_frequencies.values())
    
    # Normalize word frequencies
    for word in word_frequencies:
        word_frequencies[word] = (word_frequencies[word] / max_frequency)
    
    sentence_scores = rank_sentences(text, word_frequencies)
    summary_sentences = heapq.nlargest(top_n, sentence_scores, key=sentence_scores.get)
    
    summary = ' '.join(summary_sentences)
    return summary

# Read Articles from CSV with multiple encoding options
def read_articles_from_csv(file_path):
    encodings = ['utf-8', 'latin1', 'windows-1252']
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df['Article'].tolist(), encoding
        except UnicodeDecodeError:
            continue
    raise ValueError("The file could not be decoded with the available encodings.")

# Model Evaluation
def evaluate_summaries(articles):
    for idx, article in enumerate(articles):
        print(f"Original Article {idx + 1}:")
        print(article)
        print("\nGenerated Summary:")
        summary = generate_summary(article)
        print(summary)
        print("\n" + "="*80 + "\n")

# Command-line Interface
def summarize_from_csv():
    file_path = input("Please enter the path to the CSV file:\n")
    try:
        articles, used_encoding = read_articles_from_csv(file_path)
        print(f"File successfully read using {used_encoding} encoding.\n")
        evaluate_summaries(articles)
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    summarize_from_csv()

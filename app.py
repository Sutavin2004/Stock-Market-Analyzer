import requests
import yfinance as yf
import json
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize Sentiment Analysis Model
sentiment_model = pipeline("sentiment-analysis")

# Replace with your NewsAPI key (Get one from https://newsapi.org/)
NEWS_API_KEY = "9f8373fd8e434bcaad34c3b5ea875508"

# Function to fetch financial news headlines from NewsAPI
def fetch_news(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&language=en&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    if "articles" in data:
        return [article["title"] for article in data["articles"][:5]]  # Get top 5 headlines
    return []

# Function to analyze sentiment of headlines
def analyze_sentiment(headlines):
    sentiments = []
    
    for headline in headlines:
        result = sentiment_model(headline)[0]
        sentiments.append({
            "headline": headline,
            "sentiment": result["label"],
            "confidence": result["score"]
        })
    
    return sentiments

# Function to fetch stock price
def fetch_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    
    if data.empty:
        return "N/A"
    
    return round(data["Close"].iloc[-1], 2)

@app.route('/analyze', methods=['GET'])
def analyze():
    ticker = request.args.get("ticker", "").upper()
    
    if not ticker:
        return jsonify({"error": "Please provide a stock ticker symbol!"}), 400
    
    try:
        headlines = fetch_news(ticker)
        sentiments = analyze_sentiment(headlines)
        stock_price = fetch_stock_price(ticker)
        
        response = {
            "ticker": ticker,
            "stock_price": stock_price,
            "sentiment_analysis": sentiments
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Stock Market Sentiment Analyzer

# Overview
Stock Market Sentiment Analyzer is an AI-powered tool designed to analyze real-time financial news sentiment for any stock ticker. Using NLP-based sentiment analysis, real-time stock price data, and semantic analysis of news headlines, this API provides insights into the market sentiment surrounding a stock.

By integrating Hugging Face NLP models, NewsAPI, and Yahoo Finance, this project helps traders, investors, and analysts make data-driven decisions.

# Features

### Real-Time Financial News Analysis
- Fetches live financial news headlines for any stock ticker using NewsAPI.
- Extracts top five headlines to determine public sentiment.

### AI-Powered Sentiment Analysis
- Utilizes Hugging Face’s Transformers model to classify headlines as Positive, Neutral, or Negative.
- Confidence scores are provided for each sentiment classification.

### Live Stock Price Retrieval
- Fetches the latest stock price data using Yahoo Finance API (`yfinance`).
- Helps correlate stock price movements with sentiment trends.

### User-Friendly API with JSON Output
- Simple Flask API with a single endpoint (`/analyze?ticker=AAPL`).
- Returns a structured JSON response with stock price, sentiment insights, and timestamp.

# Technology Stack

### Programming Languages
- **Python 3.9.13**: Primary language for API and sentiment processing.

### Frameworks and Libraries
- **Flask**: For REST API development.
- **Hugging Face Transformers**: Pre-trained sentiment analysis model.
- **NewsAPI**: Fetches live financial news headlines.
- **Yahoo Finance (`yfinance`)**: Retrieves real-time stock prices.
- **Requests and JSON**: For handling API requests and responses.

# Installation

### Clone the Repository
```bash
git clone https://github.com/Sutavin2004/Stock-Market-Sentiment-Analyzer.git
cd Stock-Market-Sentiment-Analyzer
```
### Create and Activate Virtual Environment (Optional but Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
If you don’t have a requirements.txt, install manually:
```bash
pip install flask requests yfinance transformers torch
```
### Set Up NewsAPI
Sign up for a free API key from NewsAPI.
Replace "your_newsapi_key_here" in app.py with your NewsAPI key.
# Usage
### Start the Flask Server
```bash
python app.py
```
The server will start at:
```bash
http://127.0.0.1:5000
```
## Analyze a Stock’s Sentiment
Endpoint
```bash
GET /analyze?ticker=<STOCK_TICKER>
```
Example Request
```bash
http://127.0.0.1:5000/analyze?ticker=TSLA
```
## Example Input and Output
### Example API Request
```http
GET http://127.0.0.1:5000/analyze?ticker=TSLA
```
### Sample JSON Response
```json
{
    "timestamp": "2025-01-12 14:35:22",
    "stock_info": {
        "ticker": "TSLA",
        "current_price": "$243.56"
    },
    "sentiment_analysis": {
        "total_headlines_analyzed": 3,
        "details": [
            {
                "headline": "Tesla’s stock rises after strong Q4 earnings report",
                "sentiment": "Positive",
                "confidence": "97.2%"
            },
            {
                "headline": "Elon Musk warns of supply chain issues impacting production",
                "sentiment": "Negative",
                "confidence": "88.5%"
            },
            {
                "headline": "Tesla expands factory in Texas to meet demand",
                "sentiment": "Positive",
                "confidence": "92.3%"
            }
        ]
    }
}
```
# Challenges and Solutions
### Live Financial News Scraping
Issue: Yahoo Finance changes its webpage structure frequently, causing scraping failures.
Solution: Replaced it with NewsAPI, which provides reliable, structured news data.

### Sentiment Accuracy
Issue: Generic sentiment models sometimes misclassify financial sentiment.
Solution: Can be improved by fine-tuning a sentiment model for financial news.

### Correlating Stock Prices with Sentiment
Issue: Stock price changes depend on multiple factors beyond sentiment.
Solution: Future enhancements could include trend analysis over time.

# Contributions
Contributions are welcome! Follow these steps:

### Fork the Repository
### Create a Feature Branch
```bash
git checkout -b feature-name
```
### Commit Your Changes
```bash
git commit -m "Add new feature"
```
### Push the Branch
```bash
git push origin feature-name
```
### Open a Pull Request
# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Future Enhancements
Add support for additional data sources beyond NewsAPI.
Develop a web-based dashboard for sentiment tracking.
Store sentiment data in a database for historical trend analysis.
Fine-tune NLP model for better financial sentiment detection.
Implement trend prediction models based on past sentiment data.

# Contact
Email: sutavin2004@gmail.com

# Stock Price App

This is a simple Streamlit app that displays stock prices using the `yfinance` package.

## How to Run Locally

### 1. Clone the repository:
   ```bash
   git clone https://github.com/dency-claris/Stock-Price.git
   ```
### 2. Navigate to the project directory:
   ```bash
   cd Stock-Price
   ```
### 3. Build and run the Docker container:
Ensure you have Docker installed and running on your system. Then, build and run the app using the following commands:
   ```bash
   docker build -t stock-price-app .
   docker run -p 8501:8501 stock-price-app
   ```
### 4. Open your browser and go to http://localhost:8501. 
   

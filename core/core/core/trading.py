import requests
import time

class TradingBot:
    def __init__(self, symbol="BTCUSDT"):
        self.symbol = symbol
        self.last_price = None

    def fetch_price(self):
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={self.symbol}"
        data = requests.get(url).json()
        return float(data["price"])

    def check_price(self):
        price = self.fetch_price()

        if self.last_price is None:
            self.last_price = price
            print("Initial price:", price)
            return

        change = (price - self.last_price) / self.last_price

        print("Price:", price, "Change:", change)

        if change < -0.01:
            print("Potential buy signal")

        if change > 0.01:
            print("Potential sell signal")

        self.last_price = price

    def run_loop(self, delay=10):
        while True:
            self.check_price()
            time.sleep(delay)

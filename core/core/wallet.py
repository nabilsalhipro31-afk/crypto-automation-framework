import requests
import time

class WalletTracker:
    def __init__(self, address, api_key="YourKey"):
        self.address = address
        self.api_key = api_key

    def fetch_transactions(self):
        url = (
            "https://api.etherscan.io/api"
            f"?module=account&action=txlist&address={self.address}&apikey={self.api_key}"
        )
        data = requests.get(url).json()
        return data.get("result", [])

    def analyze_transactions(self, txs):
        summary = {
            "count": len(txs),
            "incoming": 0,
            "outgoing": 0
        }

        for tx in txs:
            if tx["to"].lower() == self.address.lower():
                summary["incoming"] += 1
            else:
                summary["outgoing"] += 1

        return summary

    def print_recent(self):
        txs = self.fetch_transactions()
        summary = self.analyze_transactions(txs[:20])

        print("Wallet summary:", summary)

    def monitor_loop(self, delay=30):
        while True:
            self.print_recent()
            time.sleep(delay)

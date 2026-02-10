from web3 import Web3
import time

class TokenMonitor:
    def __init__(self, rpc="https://rpc.ankr.com/eth"):
        self.w3 = Web3(Web3.HTTPProvider(rpc))

    def get_latest_block(self):
        return self.w3.eth.block_number

    def get_block(self, block_number):
        return self.w3.eth.get_block(block_number, full_transactions=True)

    def analyze_tx(self, tx):
        if tx.to is None:
            return {
                "type": "contract_creation",
                "hash": tx.hash.hex()
            }
        return None

    def scan_once(self):
        block_number = self.get_latest_block()
        block = self.get_block(block_number)

        results = []
        for tx in block.transactions:
            analysis = self.analyze_tx(tx)
            if analysis:
                results.append(analysis)

        for r in results:
            print("Detected:", r)

    def run_loop(self, delay=5):
        while True:
            self.scan_once()
            time.sleep(delay)

from core.monitor import TokenMonitor
from core.wallet import WalletTracker
from core.trading import TradingBot

def main():
    print("Starting crypto automation framework")

    monitor = TokenMonitor()
    tracker = WalletTracker("0x0000000000000000000000000000000000000000")
    trader = TradingBot("BTCUSDT")

    # exemples d’appels
    monitor.scan_once()
    tracker.print_recent()
    trader.check_price()

if __name__ == "__main__":
    main()

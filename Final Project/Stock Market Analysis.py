import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


class StockMarketAnalysis:

    def __init__(self):
        self.data = None
        self.symbol = None


    
    def download_data(self):
        self.symbol = input("Enter stock symbol (Example: AAPL, TSLA, RELIANCE.NS): ")
        start = input("Enter start date (YYYY-MM-DD): ")
        end = input("Enter end date (YYYY-MM-DD): ")

        try:
            self.data = yf.download(self.symbol, start=start, end=end)

            if self.data.empty:
                print("No data found! Check symbol or dates.")
            else:
                print("Data downloaded successfully!")

        except Exception as e:
            print("Error while downloading data:", e)

    
    def show_data(self):
        if self.data is None or self.data.empty:
            print("Please download data first.")
            return

        print("\n--- STOCK DATA ---")
        print(self.data.head())


    
    def close_price_plot(self):
        if self.data is None or self.data.empty:
            print("Download data first.")
            return

        plt.figure(figsize=(10,5))
        plt.plot(self.data["Close"], label="Close Price")
        plt.title(f"{self.symbol} - Closing Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        plt.show()


    
    def moving_average(self):
        if self.data is None or self.data.empty:
            print("Download data first.")
            return

        self.data["MA20"] = self.data["Close"].rolling(20).mean()
        self.data["MA50"] = self.data["Close"].rolling(50).mean()

        plt.figure(figsize=(10,5))
        plt.plot(self.data["Close"], label="Close Price")
        plt.plot(self.data["MA20"], label="20 Day MA")
        plt.plot(self.data["MA50"], label="50 Day MA")
        plt.title("Moving Average Analysis")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        plt.show()


    
    def volume_plot(self):
        if self.data is None or self.data.empty:
            print("Download data first.")
            return

        if "Volume" not in self.data.columns:
            print("Volume data not available for this stock.")
            return

        plt.figure(figsize=(10,5))
        plt.plot(self.data.index, self.data["Volume"], label="Volume")
        plt.title(f"{self.symbol} - Trading Volume")
        plt.xlabel("Date")
        plt.ylabel("Volume")
        plt.legend()
        plt.tight_layout()
        plt.show()


    
    def stock_summary(self):
        if self.data is None or self.data.empty:
            print("Download data first.")
            return

        print("\n--- STOCK SUMMARY ---")
        print("Highest Price:", round(self.data["High"].max(), 2))
        print("Lowest Price:", round(self.data["Low"].min(), 2))
        print("Average Closing Price:", round(self.data["Close"].mean(), 2))
        print("Total Volume:", int(self.data["Volume"].sum()))


    
    def menu(self):
        while True:
            print("\n====== STOCK MARKET ANALYSIS MENU ======")
            print("1. Download Stock Data")
            print("2. Show Data")
            print("3. Closing Price Graph")
            print("4. Moving Average Chart")
            print("5. Volume Chart")
            print("6. Stock Summary")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.download_data()
            elif choice == "2":
                self.show_data()
            elif choice == "3":
                self.close_price_plot()
            elif choice == "4":
                self.moving_average()
            elif choice == "5":
                self.volume_plot()
            elif choice == "6":
                self.stock_summary()
            elif choice == "7":
                print("Thank you for using Stock Market Analyzer!")
                break
            else:
                print("Invalid choice! Try again.")



if __name__ == "__main__":
    app = StockMarketAnalysis()
    app.menu()
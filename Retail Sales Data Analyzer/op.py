
import os
from typing import Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


class RetailAnalyzer:
    REQUIRED_COLUMNS = ["Date", "Product", "Category", "Price", "Quantity Sold"]

    def __init__(self, file_path: Optional[str] = None):
        self.data: Optional[pd.DataFrame] = None
        self.last_filtered: Optional[pd.DataFrame] = None
        self.last_plot = None

        if file_path:
            self.load_data(file_path)

    def load_data(self, file_path: str) -> bool:
        if not os.path.exists(file_path):
            print("File not found.")
            return False

        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            print(f"Failed to read CSV: {e}")
            return False

        missing = [c for c in self.REQUIRED_COLUMNS if c not in df.columns]
        if missing:
            print("Missing required columns:", missing)
            return False

        df.columns = [c.strip() for c in df.columns]
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
        df["Quantity Sold"] = pd.to_numeric(df["Quantity Sold"], errors="coerce")
        df["Total Sales"] = df["Price"] * df["Quantity Sold"]

        self.data = df
        self.last_filtered = df

        print("Dataset loaded successfully!")
        print("\nMissing values per column:")
        print(df.isnull().sum())
        return True

    def show_missing_rows(self):
        if self.data is None:
            print("No dataset loaded.")
            return
        missing_rows = self.data[self.data.isnull().any(axis=1)]
        print(missing_rows)

    def fill_missing_with_mean(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())

        self.data["Date"] = self.data["Date"].fillna(method="ffill").fillna(method="bfill")
        self.data["Product"] = self.data["Product"].fillna("Unknown")
        self.data["Category"] = self.data["Category"].fillna("Unknown")

        print("Missing values filled.")

    def drop_missing_rows(self):
        if self.data is None:
            print("No dataset loaded.")
            return

        before = len(self.data)
        self.data.dropna(inplace=True)
        after = len(self.data)

        print(f"Dropped {before - after} rows.")

    def calculate_metrics(self, df=None) -> dict:
        if df is None:
            df = self.data

        if df is None or df.empty:
            return {}

        total_sales = df["Total Sales"].sum()
        avg_sales = df["Total Sales"].mean()

        popular_product = df.groupby("Product")["Quantity Sold"].sum().sort_values(ascending=False)
        top_category = df.groupby("Category")["Total Sales"].sum().sort_values(ascending=False)

        monthly_sales = df.set_index("Date").resample("M")["Total Sales"].sum()
        growth = (
            monthly_sales.pct_change().fillna(0).iloc[-1] * 100
            if len(monthly_sales) > 1 else 0
        )

        return {
            "total_sales": float(total_sales),
            "average_sales": float(avg_sales),
            "most_popular_product": popular_product.index[0] if not popular_product.empty else None,
            "top_category": top_category.index[0] if not top_category.empty else None,
            "last_month_growth_pct": float(growth)
        }

    def display_summary(self):
        metrics = self.calculate_metrics(self.last_filtered)

        print("\n========== SUMMARY ==========")
        for key, value in metrics.items():
            print(f"{key}: {value}")
        print("==============================\n")

    def filter_data(self, category=None, start_date=None, end_date=None):
        if self.data is None:
            raise RuntimeError("No dataset loaded.")

        df = self.data.copy()

        if category:
            df = df[df["Category"].str.lower() == category.lower()]
        if start_date:
            df = df[df["Date"] >= pd.to_datetime(start_date)]
        if end_date:
            df = df[df["Date"] <= pd.to_datetime(end_date)]

        self.last_filtered = df
        return df

    def plot_sales_by_category(self, df=None):
        df = df or self.last_filtered
        if df is None or df.empty:
            print("No data available to plot.")
            return

        plt.close()
        category_sales = df.groupby("Category")["Total Sales"].sum().reset_index()

        plt.figure(figsize=(8, 5))
        sns.barplot(data=category_sales, x="Category", y="Total Sales")
        plt.title("Sales by Category")
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.last_plot = plt.gcf()
        plt.show()

    def plot_sales_trend(self, df=None):
        df = df or self.last_filtered
        if df is None or df.empty:
            print("No data available to plot.")
            return

        plt.close()
        monthly = df.set_index("Date").resample("M")["Total Sales"].sum().reset_index()

        plt.figure(figsize=(8, 5))
        sns.lineplot(data=monthly, x="Date", y="Total Sales", marker="o")
        plt.title("Sales Trend Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()

        self.last_plot = plt.gcf()
        plt.show()

    def plot_price_quantity_heatmap(self, df=None):
        df = df or self.last_filtered
        if df is None or df.empty:
            print("No data available to plot.")
            return

        plt.close()
        corr = df[["Price", "Quantity Sold", "Total Sales"]].corr()

        plt.figure(figsize=(6, 4))
        sns.heatmap(corr, annot=True)
        plt.title("Correlation Heatmap")
        plt.tight_layout()

        self.last_plot = plt.gcf()
        plt.show()

    def save_last_plot(self, filename: str):
        if self.last_plot is None:
            print("No plot to save.")
            return
        self.last_plot.savefig(filename)
        print(f"Plot saved as: {filename}")


def main():
        analyzer = RetailAnalyzer()
        print("***** Retail Sales Data Analyzer *****")

        while True:
            print("""
1. Load Dataset
2. Show Missing Data
3. Fill Missing Values
4. Drop Missing Rows
5. Show Summary (Filtered)
6. Filter Data
7. Plot: Sales by Category
8. Plot: Sales Trend
9. Plot: Correlation Heatmap
10. Save Last Plot
11. Exit
""")

            choice = input("Enter choice: ").strip()

            try:
                if choice == "1":
                    analyzer.load_data(input("CSV path: ").strip())

                elif choice == "2":
                    analyzer.show_missing_rows()

                elif choice == "3":
                    analyzer.fill_missing_with_mean()

                elif choice == "4":
                    analyzer.drop_missing_rows()

                elif choice == "5":
                    analyzer.display_summary()

                elif choice == "6":
                    category = input("Category (blank to skip): ").strip()
                    start = input("Start date YYYY-MM-DD (blank skip): ").strip()
                    end = input("End date YYYY-MM-DD (blank skip): ").strip()

                    df = analyzer.filter_data(
                        category or None,
                        start or None,
                        end or None
                    )
                    print("Filtered rows:", len(df))
                    print(df.head())

                elif choice == "7":
                    analyzer.plot_sales_by_category()

                elif choice == "8":
                    analyzer.plot_sales_trend()

                elif choice == "9":
                    analyzer.plot_price_quantity_heatmap()

                elif choice == "10":
                    fname = input("File name (e.g., plot.png): ").strip()
                    analyzer.save_last_plot(fname)

                elif choice == "11":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Try again.")

            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    main()

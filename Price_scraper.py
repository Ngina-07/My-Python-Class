import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def get_exchange_rate(base_currency="GBP", target_currency="USD"):
    """Fetch live exchange rate using exchangerate-api.com (open endpoint)."""
    try:
        url = f"https://open.er-api.com/v6/latest/{base_currency}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("result") == "success":
            rate = data["rates"].get(target_currency)
            if rate:
                return rate
        print(f"Failed to fetch rate for {target_currency}. Defaulting rate to 1.0.")
        return 1.0
    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching exchange rate: {e}")
        return 1.0

def scrape_books_and_convert(target_currency="USD"):
    url = "https://books.toscrape.com/"
    
    # 1. Fetch Webpage with Error Handling
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to target website: {e}")
        return

    # 2. Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("article", class_="product_pod")
    
    # 3. Get Exchange Rate (Books.toscrape uses GBP £)
    rate = get_exchange_rate("GBP", target_currency)
    print(f"Current Exchange Rate (GBP to {target_currency}): {rate}")

    # 4. Extract and Clean Data
    data = []
    for product in products:
        # Extract title
        title = product.h3.a["title"]
        
        # Extract and clean price string (e.g., '£51.77' -> 51.77)
        raw_price = product.find("p", class_="price_color").text
        price_match = re.search(r"[\d.]+", raw_price)
        
        if price_match:
            price_gbp = float(price_match.group())
            converted_price = round(price_gbp * rate, 2)
            
            data.append({
                "Book Title": title,
                "Price (GBP)": price_gbp,
                f"Price ({target_currency})": converted_price
            })

    # 5. Process & Display with Pandas
    df = pd.DataFrame(data)
    
    print("\n" + "="*50)
    print(f" SCRAPED PRODUCT DATA ({len(df)} Products)")
    print("="*50)
    print(df.to_string(index=False))

    # 6. Save to CSV
    output_filename = "scraped_products.csv"
    df.to_csv(output_filename, index=False)
    print(f"\nData successfully saved to '{output_filename}'")

if _name_ == "_main_":
    # You can change 'USD' to 'KES', 'EUR', etc.
    scrape_books_and_convert(target_currency="USD")
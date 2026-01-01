import requests
from bs4 import BeautifulSoup
import csv
import datetime

# نستخدم HTTPS ومحرك LXML الأقوى
url = "https://books.toscrape.com/"

# بنعرف نفسنا كمتصفح عشان الموقع ميعملش بلوك
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

filename = "products_data.csv"
header = ['Product Name', 'Price', 'Availability', 'Date Scraped']

print(f"🔄 Connecting to {url}...")

try:
    # بنبعت الهيدر (البطاقة الشخصية) مع الطلب
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # استخدام lxml بدلاً من html.parser لدقة أعلى
        soup = BeautifulSoup(response.text, 'lxml')
        
        books = soup.find_all('article', class_='product_pod')
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            
            count = 0
            for book in books:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='instock availability').text.strip()
                today = datetime.date.today()
                
                writer.writerow([title, price, availability, today])
                count += 1
                
        if count > 0:
            print(f"✅ Success! Scraped {count} items.")
            print(f"📂 Data saved to '{filename}' inside the folder.")
        else:
            print("⚠️ Connected, but found 0 items. Check the parsers.")
            
    else:
        print("❌ Failed to retrieve the webpage.")

except Exception as e:
    print(f"❌ Error: {e}")
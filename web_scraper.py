# pkg install python
# pkg install python-dev

# pip install requests
# pip install beautifulsoup4
# pip install fake_useragent

# run langsung
# python web_scraper.py <<< $'banyak\ncauwarna.txt\nreferer.txt\n10000'



import requests
from bs4 import BeautifulSoup
import time
import random
from fake_useragent import UserAgent

# Membuat instance UserAgent
ua = UserAgent()

# Menghasilkan user agent secara acak
def generate_user_agent():
    return ua.random

# Membuat daftar 25 user agent yang berbeda
user_agents = [generate_user_agent() for _ in range(25)]

# Fungsi untuk mendapatkan alamat IP acak dari berbagai negara
def get_random_ip():
    response = requests.get("https://geolocation-db.com/json/")
    data = response.json()
    return data['IPv4']

if __name__ == "__main__":
    url_choice = input("Apakah Anda ingin membuka satu URL artikel atau banyak? (satu/banyak): ")

    if url_choice == "satu":
        url = input("Masukkan URL artikel: ")
        urls = [url]
    elif url_choice == "banyak":
        file_path = input("Masukkan alamat file (.txt) yang berisi list URL artikel: ")
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    else:
        raise ValueError("Pilihan tidak valid. Pilih antara satu atau banyak.")

    referer_file_path = input("Masukkan alamat file (.txt) yang berisi list referer URLs: ")
    with open(referer_file_path, 'r') as referer_file:
        referer_urls = [line.strip() for line in referer_file if line.strip()]

    limit = int(input("Masukkan limit: "))

    print("WEB Viewer")
    count = len(urls)
    for i in range(limit):
        article_number = i + 1
        url = urls[i % count]

        headers = {
            'User-Agent': user_agents[random.randint(0, len(user_agents) - 1)],
            'Referer': referer_urls[random.randint(0, len(referer_urls) - 1)],
            'X-Forwarded-For': get_random_ip()  # Menambahkan header X-Forwarded-For dengan alamat IP acak
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            if title_tag is not None:
                article_title = title_tag.text
                print(f"=> {article_number}: {article_title}")
            else:
                print(f"=> {article_number}: Gagal mengambil artikel.")
        except requests.exceptions.RequestException as e:
            print(f"=> {article_number}: Terjadi kesalahan: {str(e)}")

        print("Tunggu 5 detik untuk artikel berikutnya...")
        print("--------------------------------------")
        time.sleep(5)

    print("Developer by @denigentarcandana")

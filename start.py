import os
import sys
import time
import platform
import random
import shutil
import signal
from termcolor import colored
from pyfiglet import Figlet
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

def generate_user_agent():
    return ua.random

def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.exceptions.RequestException as e:
        print("Tidak dapat terhubung ke internet. Periksa koneksi Anda.")
        return False

if platform.system() == "Linux" and "TERMUX" in os.environ:
    os.system("termux-setup-storage")
    os.system("termux-setup-terminal -q --size 40x120")

user_agents = [generate_user_agent() for _ in range(1000)]

def signal_handler(sig, frame):
    print(colored("Proses dihentikan.", "yellow") + colored(" Aku hanya bisa pergi jika kamu menghentikanku.\n", "green"))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

random_ip = None

def get_random_ip():
    global random_ip
    
    try:
        with open("ip.txt", "r") as file:
            ip_list = [line.strip() for line in file if line.strip()]
        random_ip = random.choice(ip_list)
        return random_ip
    except FileNotFoundError:
        print("File 'ip.txt' tidak ditemukan.")
        return None

def track_ip():
    if random_ip:
        url = f"https://ip-api.com/json/{random_ip}"
        response = requests.get(url)
        data = response.json()

        country = data.get('country')
        city = data.get('city')
        location_code = data.get('region')

        return country, city, location_code
    else:
        return None

def show_banner():
    f = Figlet(font='slant')
    banner_text = f.renderText("Web Scraper")
    terminal_width = shutil.get_terminal_size().columns
    max_banner_width = min(terminal_width, 80)
    f = Figlet(font='slant', width=max_banner_width)
    banner_text = f.renderText("Web Scraper")
    print(colored(banner_text, 'blue'))

def scrape_article(url, article_number, referer_urls, user_agents):
    random_ip = get_random_ip()
    if random_ip is None:
        return
    try:
        user_agent = random.choice(user_agents)
        headers = {
            "User-Agent": user_agent,
            "Referer": random.choice(referer_urls),
            "X-Forwarded-For": get_random_ip()
        }
        print(colored(f"User-Agent: {user_agent}", "red"))
        print(colored(f"Referer: {headers['Referer']}", "yellow"))
        print(colored(f"X-Forwarded-For: {headers['X-Forwarded-For']}", "green"))
        print()

        print(colored(f"SCRAPING URL {article_number}: {url}", "blue"))

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.find('title')

        if title_tag is not None:
            article_title = title_tag.text
            print(f"=> {colored(article_number, 'green')}: {colored(article_title, 'cyan')}")
            print(colored("Aku ingin memberikanmu artikel yang indah seperti hatimu.\n", "magenta"))
        else:
            print(f"=> {colored(article_number, 'green')}: {colored('Gagal mengambil artikel.', 'red')}")
            print(colored("Mungkin hatiku belum cukup untukmu.\n", "magenta"))

    except requests.exceptions.RequestException as e:
        print(f"=> {colored(article_number, 'green')}: {colored('Gagal mengambil artikel.', 'red')}")
        print(colored("Terjadi kesalahan saat melakukan permintaan HTTP:", "magenta"))
        print(colored(str(e), "red"))


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    if not check_internet_connection():
        print(colored("Tidak ada koneksi internet.", "red") + colored(" Hati-hati ya, hatiku bisa meleleh padamu.\n", "green"))

    while True:
        url_choice = input(colored("Apakah kamu ingin membuka satu URL artikel atau banyak? ", "green") + colored(" Kamu tahu, jika kamu pilih 'satu' maka hatiku hanya akan terbuka untukmu, tapi jika kamu pilih 'banyak' hatiku akan meleleh padamu.\nJadi, apa pilihanku di hatimu? ", "magenta") + colored("(satu/banyak): ", "yellow"))
    
        if url_choice == "satu":
            url = input(colored("Masukkan URL artikel: ", "cyan") + colored(" Kamu sungguh pandai memilih, hatiku hanya akan terbuka untukmu.\n", "green"))
            urls = [url]
            break
        elif url_choice == "banyak":
            file_path = input(colored("Masukkan alamat file (.txt) yang berisi list URL artikel: ", "cyan") + colored(" Hati-hati ya, hatiku bisa meleleh padamu.\n", "green"))
    
            try:
                with open(file_path, 'r') as file:
                    urls = [line.strip() for line in file if line.strip()]
                break
            except FileNotFoundError:
                print(colored("File tidak ditemukan.", "red") + colored(" Hati-hati ya, jangan sampai membuat hatiku hancur.\n", "green"))
        else:
            print(colored("Pilihan tidak valid. Pilih antara satu atau banyak.", "red") + colored(" Aku hanya bisa memilih antara hatimu yang satu atau hatimu yang banyak.\n", "green"))
    
    while True:
        referer_file_path = input(colored("Masukkan alamat file (.txt) yang berisi list referer URLs: ", "yellow") + colored(" Ini menarik, apa referer URLs yang ingin kamu bagikan padaku?\n", "green"))
    
        try:
            with open(referer_file_path, 'r') as referer_file:
                referer_urls = [line.strip() for line in referer_file if line.strip()]
            break
        except FileNotFoundError:
            print(colored("File tidak ditemukan.", "red") + colored(" Hati-hati ya, hatiku bisa meleleh padamu.\n", "green"))
            
    limit = int(input(colored("Masukkan limit: ", "yellow") + colored(" Hmm, berapa banyak yang ingin kamu ambil? ", "green")))
    show_banner()
    print(colored("Meluncurkan proses scraping...", "blue") + colored(" Jaga hatiku agar tetap berdetak untukmu.\n", "green"))
    
    if url_choice == "satu":
        scrape_article(urls[0], 1, referer_urls, user_agents)
        print()
    else:
        for index, url in enumerate(urls[:limit], start=1):
            scrape_article(url, index, referer_urls, user_agents)
            print()
    
            if index < len(urls[:limit]):
                print(colored("Jeda waktu 30 detik sebelum melanjutkan ke URL berikutnya...", "blue") + colored(" Hati-hati ya, jangan tinggalkan hatiku terluka.\n", "green"))
                time.sleep(30)
    
    print(colored("Proses scraping selesai.", "blue") + colored(" Hati-hati ya, jangan tinggalkan hatiku terluka.\n", "green"))
    

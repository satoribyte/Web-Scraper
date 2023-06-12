# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def generate_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Mencari semua elemen <loc> di sitemap
    loc_elements = soup.find_all('loc')

    # Membuat daftar URL dari elemen <loc>
    urls = [elem.text for elem in loc_elements]

    return urls

def save_to_file(urls, file_name):
    with open(file_name, 'w') as file:
        for url in urls:
            file.write(url + '\n')

def main():
    # Input alamat sitemap
    sitemap_url = input("Masukkan alamat sitemap: ")

    # Menghasilkan sitemap
    urls = generate_sitemap(sitemap_url)

    # Menyimpan sitemap ke file
    file_name = input("Masukkan nama web (nama_web.txt): ")
    save_to_file(urls, file_name)

    print("Sitemap telah dibuat dan disimpan di", file_name)

if __name__ == '__main__':
    main()

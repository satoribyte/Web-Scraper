
     
     
                                      ,▄▄▓█████▄▄▄,
                                    ┌▓███████████████▄,
                                ,▄▄▓████████████████████▄,
                              ,▓▓█████████████████████████▄
                             ║▓█████████▀▀▀▀▀▀▀▀▀██████████⌡
                             ▓███████▀▒▒▒▒▒▒▒▒▒▒▒ÑÑÑ▓██████U
                             ▓██████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒Ñ▓█████▌
                             ▐█████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒Ñ@▓▓▓███▌
                              ▀███▒M▒▒▒▒▄▒▒░░░░▒@@▓▓▓▓▓▓██▀
                               ▀█▌Ñ▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▄▄▄▒▒▓█▀
                              ╔N▀▌▒▒▒▀▒▀▒▒▒▒▒▒M▒▒▒▀▒▒▒▒▒▓▒▓
                              ╠▒░$▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒
                              └▒▒▓▒▒░░░▒░▒▒░▒░▒▒▒▒▒░░▒▒▒@▒M
                               ║▒╣▒▒░░░ ░░▒▒▒▒▒▒▒▒░░░▒▒▒▓▒⌡
                                "╘▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
                                  ╚▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
                                   ╙▓▒▒▒▒▒░░░▒▒░▒▒▒▒▒▓▓
                                   /$▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓Ñ▓
                                 ,q░╞▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒
                            ,╓α▒░▒▒░ └%▄▒▒▒▒▒▒▒▒Ñ▒▒▒▓▌▒╡▒▒M╖,
                       ,╓α▒░▒░░░░▒▒▒⌂░░`▀▓▓▒▒▒▒▒▒▒@▓▓▒▓▀▒▒▒▒▒▒DN┬,
                   ,⌐▒░▒▒░░░▒░░▒░░▒▒▒M╣░░»░▀▓▓▒╣▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒DW,
                 «▒░░░ ░▒▒░░▒▒░░░░░░░▒▒▒▒░@╖▓╣▓▓▀░▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒N,
               ╓▒░░░░░ ░▒▒▒░▒▒▒░░░░░░░░░░╘╣▓▓▓▓▒░▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
               ░ ░░ ░▒▒░░▒▒░░▒▒▒░░░░░░░░░░░╙▓▓▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒
     
     
              ,           ,       ,  ,,,     ,,,       ,,                 ,,
              █    ██▄   ║█▌    ╒██  █▀"▀▀█  █▀""▀█  ▄█▀`▀▀▄  ██▄   █H ,█▀``▀█
              █   █▀ █   ║▌▀▌  ┌█▐█  █▄▄▄▄▀  █∩  ,█∩ █     █∩ █Ü▀▌  █H █▌
              █  ▄█▄▄▄█  ║█ ▀▄ █.▐█  █   "█  █▀▀▀█   █     █∩ █U ╙█,█H █▌  ▀▀█⌡
         ▀█▄,▄█ ╓█    ▀█ ║█  ██" ▐█  █▄▄▄▄█  █∩  └█µ ▀█▄,▄█▀  █U   ▀█H `█▄,,▄█U
          YT : Deni Gentar Candana
     
    

# Web Scraper

Web Scraper is a Python program used to extract data from websites. This program utilizes libraries such as requests, BeautifulSoup, and fake_useragent for efficient web scraping.

## Usage

1. Ensure you have Python installed on your computer.
2. Clone this repository to your local machine.
3. Open the terminal and navigate to the project directory.
4. Install the dependencies by running the following command:

`pip install -r requirements.txt`

5. Customize the code in the `web_scraper.py` file according to your needs. You can set the article URL(s), referer URLs, and data extraction limits.
6. Run the program by executing the following command:

`python web_scraper.py`

7. Follow the prompts displayed in the terminal to select either a single article URL or multiple article URLs.
8. The program will start scraping and display the extracted article information from the website.

## How It Works

1. The program generates a random user agent using the `fake_useragent` library. This user agent is used to provide variation and anonymity when making requests to the server.
2. If the user chooses the option for multiple article URLs, the program reads the list of article URLs from the specified file.
3. The program also reads the list of referer URLs from the specified file to be used as references when making requests.
4. In each iteration, the program randomly selects a user agent and referer URL from the provided lists.
5. The program sends HTTP requests using the `requests` library with headers set according to the selected user agent and referer URL.
6. The response is parsed using the `BeautifulSoup` library to extract the article titles from the web page.
7. The article titles are then displayed in the terminal.
8. After each iteration, the program waits for 5 seconds before proceeding to the next article.

## Impact

This Web Scraper program allows you to easily retrieve information from websites automatically. You can use it for various purposes, such as:

- Gathering article data from different websites for analysis or research.
- Monitoring changes on specific websites and obtaining the latest information periodically.
- Extracting product information from e-commerce sites for price comparison or obtaining data for market analysis.

However, it's important to use it ethically and comply with the applicable rules. Make sure you have permission to access and retrieve data from the targeted websites. Also, be mindful of the limitations and policies of the websites regarding data scraping.

Developed by [@denigentarcandana.id](https://www.instagram.com/denigentarcandana.id/)

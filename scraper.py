import requests
from bs4 import BeautifulSoup

# put your list of URLs to scrape
urls = [
'URL HERE' 
]

with open('content.txt', 'a', encoding='utf-8') as file:
    for url in urls:    
        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')

            all_text = soup.get_text()

            all_text = ' '.join(all_text.split())

            file.write(all_text + '\n\n')  

            print('Extraction complete. The text from {} is saved in narrative.txt.'.format(url))
        else:
            print('Failed to retrieve the web page from {}.'.format(url))

print('All text is saved in narrative.txt.')

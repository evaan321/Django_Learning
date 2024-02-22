from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
def myScraper(request):
    url = 'https://fbcaptionbangla.com/best-sad-status-captions-in-bangla/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify())
    n=0
    headlines = []
    for headline_element in soup.find_all('p'):
        
        headline_text = headline_element.get_text(strip=True) 
        headlines.append(headline_text)
        
    print(headlines)
    return render(request, 'index.html', {'data': headlines ,'size': headlines})

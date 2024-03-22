from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# def myScraper(request):
#     url = 'https://www.rokomari.com/book/968/jochna-o-jononir-golpo'
#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, 'html.parser')

#     # print(soup.prettify())
#     n=0
#     headlines = []
#     for headline_element in soup.find_all('p' , class_ = 'review-text'):
        
#         headline_text = headline_element.get_text(strip=True) 
#         headlines.append(headline_text)
        
#     print(headlines)
#     return render(request, 'index.html', {'data': headlines ,'size': headlines})


# def myScraper(request):
#     base_url = 'https://www.ittefaq.com.bd/'
#     headlines = []

#     for page_num in range(1, 5):  # Scrape up to page 5
#         url = base_url if page_num == 1 else f'{base_url}?page={page_num}'
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # ... (The rest of your scraping code to extract titles)

#     return render(request, 'index.html', {'data': headlines, 'size': len(headlines)})


# def myScraper(request):
#     url = 'https://www.ittefaq.com.bd/'
#     headlines = []

#     # Loop through multiple pages if there is pagination
#     for page_number in range(1, 50):  # Adjust the range based on the number of pages
#         page_url = f'{url}?page={page_number}'  # Update the URL with the page number
#         response = requests.get(page_url)

#         soup = BeautifulSoup(response.text, 'html.parser')

#         for headline_element in soup.find_all('a', class_="link_overlay"):
#             headline_text = headline_element.get_text(strip=True)
#             headlines.append(headline_text)

#         print(headlines)
#         return render(request, 'index.html', {'data': headlines, 'size': len(headlines)})


def myScraper(request):
    base_url = 'https://bonikbarta.net'
    max_pages = 2  # Set the maximum number of pages to scrape
    headlines = []

    for page_num in range(1, max_pages + 1):
        url = base_url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Assuming the structure to get headlines remains the same:
        for headline_element in soup.find_all('h4','caption-title'): 
            headline_text = headline_element.get_text(strip=True) 
            headlines.append(headline_text)

    return render(request, 'index.html', {'data': headlines, 'size': len(headlines)})
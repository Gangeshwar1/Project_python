# if you want to scrape website
# 1. use the API 
# HTML web scrapping using some tools like
# pip install requests 
# pip install bs4 
# pip install html5lib
from turtle import clear
import requests 
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"

# step 1: get the HTML
r = requests.get(url)
htmlContent = r.content 
# print(htmlContent)

# step 2: parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())

# step 3: HTML tree traversal
# commonly  used type of object
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. Navigablestring
# print(type(soup)) # 3. BeautifulSoup
# 4. Comment

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p.string)
# exit()

# Get the titile og HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(soup)
# Get all the anchors tags from the page
anchors = soup.find_all('a')
# print(anchors)

# Get first element in the HTML page
# print(soup.find('p'))

# # Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# # find all the elements with class lead
# print(soup.find_all("p", class_= "lead"))

# # Get the text from the tags/soup
# print(soup.find('p').get_text()
# print(soup.get_text())

# all_links = set()
# # Get all the links on the pages
# for link in anchors:
#     if(link.get('href') != '#'):
#         linktest = "https://codewithharry.com" + link.get('href')
#         all_links.add(link)
        #print(linktest)

navContent= soup.find(id="nav-content")
# .contents - a tag's children are available in a list
# .children - a tag's children are available as a generator

# for elem in navContent.contents:
#     print(elem)
# for items in navContent.strings:
#     print(items)

# for items in navContent.stripped_strings:
#     print(items)

# print(navContent.parent)
# for item in navContent.parents:
#     print(item.name)

# print(navContent.next_sibling.next_sibling)
# print(navContent.previous_sibling.previous_sibling)

elem = soup.select('#loginModal')
print(elem)



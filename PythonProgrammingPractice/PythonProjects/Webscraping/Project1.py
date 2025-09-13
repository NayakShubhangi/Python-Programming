# WEBSCRAPING
# Webscraping is the process of extracting data from websites.
# In python, it usually involves:
#       1. Fetching the webpage (HTML content)
#       2. Passing the HTML
#       3. Extracting the desired information


import requests
from bs4 import BeautifulSoup

# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# quotes = soup.find_all("div", class_="quote")   # class is already a keyword, so class_ is used instead
# for quote in quotes:
#     text = quote.find("span", class_="text").text
#     author = quote.find("small", class_="author").text
#     print(text+" "+author+"\n")


# TODO TASK TWO: (?)
# Using webscraping, print the author of Python and the title "Languages influenced by Python",
# along with the programming languages listed (ONLY THE LANGUAGES, not the sentences they're in
# (they're the first word of each sentence))
# 
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# content = soup.find("div", class_="mw-content-ltr")
# paragraphs = content.find_all("p")
# for id, p in enumerate(paragraphs):
#     if id == 1 or id == 2:
#         if p.text.strip():
#             print(p.text.strip()+"\n")
# data = soup.find_all("div", "mw-heading")
# for d in data:
#     heading = d.find("h2", id="Languages_influenced_by_Python")
#     if heading:
#         print(heading.text)

# --------------
# content2 = soup.find("div", class_="mw-content-ltr")
# sentences = content2.find_all("ul")
# for sentence in sentences:
#     list_thing = sentence.find_all("li")
#     for lt in list_thing:
#         things = lt.find_all("a")
#         for thing in things:
#             li_items = []
#             li_items.append(thing.text)
# print(li_items)
# table = soup.find("table", class_="infobox vevent")
# languages = []
# if table:
#     rows = table.find_all("tr")
#     for row in rows:
#         header = row.find("th")
#         if header and "Influenced" in header.text:
#             links = row.find("td").find_all("a")
#             for link in links:
#                 languages.append(link.text)
# print(languages)

# infobox = soup.find("table", {"class": lambda x: x and "infobox" in x})
# languages = []
# if infobox:
#     rows = infobox.find_all("tr")
#     for row in rows:
#         header = row.find("th")
#         if header and "Influenced" in header.get_text():
#             td = row.find("td")
#             if td:
#                 for a in td.find_all("a"):
#                     languages.append(a.get_text(strip=True))
#                 break
# print(languages)

# url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# infobox = soup.find("table", {"class": lambda x: x and "infobox" in x})
# languages = []
# if infobox:
#     for row in infobox.find_all("tr"):
#         header = row.find("th")
#         print(f"Header: {header}")
#         if header == header.get_text() and "Influenced" == header.get_text():
#             td = row.find("td")
#             print(f"Td: {td}")
#             if td:
#                 for a in td.find_all("a"):
#                     languages.append(a.get_text(strip=True))
#             break
# print(languages)


# TASK THREE: (DONE)
# Get the title "Python Needs You" along with the paragraph below it
# https://www.python.org/doc/

# url = "https://www.python.org/doc/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# content = soup.find("div", class_="python-needs-you-widget")
# title = content.find("h2", class_="widget-title").text
# print(title)
# paragraphs = content.find_all("p")
# for id, paragraph in enumerate(paragraphs):
#     if id == 0:
#         print(paragraph.text)


import os
url = "https://docs.python.org/3/contents.html"
def retrieve_elements(ul_tag):
    items = []
    if ul_tag:
        for li in ul_tag.find_all("li", recursive=False):
            link_tag = li.find("a")
            if link_tag:
                key = link_tag.text.strip()
                item_data = {"Key": key}
                nested_ul = li.find("ul")
                if nested_ul:
                    item_data["sub_items"] = retrieve_elements(nested_ul)
                else:
                    item_data["sub_items"] = []
                items.append(item_data)
    return items
# TASK ONE: (DONE)
# Use recursion in the function and use it inside of loops rather than just looping over and over
# to make it more efficient


def write_in_file(data, filename="Python_Documentation_Info.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        def write_level(items, indent_level=0):
            indent_char = "  "
            for item in items:
                indent = indent_char * indent_level
                file.write(f"{indent}Key: {item['Key']}\n")
                if "sub_items" in item and item["sub_items"]:
                    file.write(f"{indent}Values:\n")
                    for sub_item in item["sub_items"]:
                        file.write(f"{indent}{indent_char}- {sub_item['Key']}\n")
                    for sub_item in item["sub_items"]:
                        if "sub_items" in sub_item and sub_item["sub_items"]:
                            write_level([sub_item], indent_level + 1)
                else:
                    file.write(f"{indent}Values: []\n")
                if indent_level == 0:
                    file.write("\n")
        write_level(data)
# TASK TWO: (DONE)
# Once the issue above has been resolved, use file handling to append the data to two .txts,
# one for the ul(s) (keys), and the other for the li(s) (values)


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
content_div = soup.find("div", class_="toctree-wrapper")
top_ul = content_div.find("ul")
data = retrieve_elements(top_ul)
write_in_file(data)
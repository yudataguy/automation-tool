from bs4 import BeautifulSoup
import requests
import re
import webbrowser
 
def openLinks(url):
    html_page = requests.get(url) #get the link
    soup = BeautifulSoup(html_page.content, 'html.parser') #parse the link content
    links = [] #empty list for store links

    first_url = "http://" + url.split('http://')[1].split('/')[0] #get the top level domain

    #Replace the next part with any specification.

    for link in soup.find_all(id=re.compile("normal")): #only get the id contains "normal" 
        for thread in link.find_all(class_=re.compile("xst")): #only get class contains "xst"
            links.append(first_url + "/" + thread.get("href")) #get the link and convert it to complete url
    
    for dvd in links:
        webbrowser.get('firefox').open_new_tab(dvd) #open url in firefox
 
openLinks("http://your-own-url") #replease any link

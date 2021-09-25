import requests
import bs4
import re


def get_links(url):
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text,'html.parser')
    print(soup,"\n-----------------------------------------------------")
    links = soup.find_all("a",attrs = {'href' : re.compile("^https://")})#https://www.geeksforgeeks.org/privacy-policy/
    #print(type(links))    #<class 'bs4.element.ResultSet'>
    #print(type(links[0]))  # <class 'bs4.element.Tag'>

    for l in links:print(l.get('href'))


def main():
    url = input()
    get_links(url)


if __name__ == "__main__":
    main()

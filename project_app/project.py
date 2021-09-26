import requests
import bs4
import re
import urllib

def get_links(url):
    try:
        resp = requests.get(url)
    except:
        return [url]
    soup = bs4.BeautifulSoup(resp.content,'html.parser')
    links = soup.find_all("a",attrs = {'href' : re.compile("^https://")})#https://www.geeksforgeeks.org/privacy-policy/
    #print(type(links))    #<class 'bs4.element.ResultSet'>
    #print(type(links[0]))  # <class 'bs4.element.Tag'>
    
    hyperlinks = []
    
    for l in links:
        hyperlinks.append(l.get('href'))
    return hyperlinks



def test_links(hyperlinks):
    wrong_urls = []
    for url in hyperlinks:
        try:
            code = urllib.request.urlopen(url).getcode()
            #print(code,url)
            if code != 200:
                wrong_urls.append(url)
        except:
            #print("camehere dude",url)
            wrong_urls.append(url)
    return wrong_urls


def main():
    url = input()
    hyperlinks = get_links(url)
    #print(hyperlinks,"\n------") #-->list
    wrong_urls = test_links(hyperlinks)
    #print(wrong_urls)

if __name__ == "__main__":
    main()

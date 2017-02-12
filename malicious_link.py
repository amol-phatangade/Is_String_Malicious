import urllib2, sys, urllib
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print('usage : ' + sys.argv[0] + ' <pdb path/ string>')
    sys.exit()

def get_urls(string):

    url = 'http://www.google.com/search?' + urllib.urlencode(string) 
    #url = sys.argv[1]
    print url

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    data = opener.open(url).read()

    #print data
    soup = BeautifulSoup(data, 'lxml')

    links = soup.find_all('div', 'g')
    for link in links:
        print(link.a.get('href')[7:])
    #exit(0)
    return links

def main():
    string = {'q': ' '.join(sys.argv[1:])}
    string['q'] = '\"' + string['q'] + '\"'
    links = get_urls(string)
    fd_malicious_links = open("malicious_link.txt", "r")
    malicious_link = fd_malicious_links.readlines()

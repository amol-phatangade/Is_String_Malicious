import urllib2, sys, urllib
from bs4 import BeautifulSoup

if len(sys.argv) < 3:
    print('usage : ' + sys.argv[0] + ' <pdb path/string> ' + '<0: With Cout / 1: Wthout Cout>')
    sys.exit()

fd_log = open("log.txt", "w")

def get_urls(string):

    url = 'http://www.google.com/search?' + urllib.urlencode(string) 
    #url = sys.argv[1]
    print url
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    data = opener.open(url).read()
    soup = BeautifulSoup(data, 'lxml')
    links = soup.find_all('div', 'g')
#    for link in links:
#        print(link.a.get('href')[7:])
    return links

def desplay_match_count(malicious_link, links):
    match_count = 0
    for i in malicious_link:
        for link in links:
            if i[:-1] in link.a.get('href')[7:]:
                match_count += 1
                print i
                write_log(i)
                write_log(": ")
                

    print match_count,"/" , len(links)
    write_log(",")
    write_log(str(match_count) + "/" + str(len(links)))
    
def write_log(data):
    
    fd_log.write(data)
    

def main():
    string = {'q': ' '.join(sys.argv[2:])}
    if int(sys.argv[1]) == 0:
        string['q'] = '\"' + string['q'] + '\"'
#    print string['q']
    fd_malicious_links = open("malicious_link.txt", "r")
    malicious_link = fd_malicious_links.readlines()
    write_log(string['q'])
    write_log(",")
    links = get_urls(string)
    match_count = desplay_match_count(malicious_link, links)
    write_log("\n")
    
    print string['q']
    if '\\' in string['q']:
        t_string = string['q'].split('\\')
        n_string = t_string[-1:][0]
#        print n_string
        n_string = n_string
        string['q'] =  n_string
        if int(sys.argv[1]) == 0:
            n_string = n_string[:-1]
            string['q'] = '\"' + n_string + '\"'
#        print string
        write_log(string['q'])
        write_log(",")
        links = get_urls(string)
        desplay_match_count(malicious_link, links)
        write_log("\n")
    fd_malicious_links.close()
    
main()

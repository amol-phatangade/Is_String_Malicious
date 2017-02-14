import urllib2, sys, urllib
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print('usage : ' + sys.argv[0] + ' <pdb path/ string>')
    sys.exit()

def	check_siteadvisor(link):
	url = 'http://www.siteadvisor.com/sites/' + link 
	#print url
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	data = opener.open(url).read()
	soup = BeautifulSoup(data, 'lxml')
	text = soup.find_all('p', 'intro')
	#print text[0]
	if "This link might be dangerous" in str(text[0]):
		return 1
	if "This link is suspicious" in str(text[0]):
		return 2
	return 3
	
def FindSubString(str1, str2):
	for i in range(0, len(str1)):
		EndFlag = 0
		k = i
		for j in range(0, len(str2)):
			if str1[k] != str2[j]:
				EndFlag = 1
				break
			k += 1
		if EndFlag == 0:
			return i + len(str2)	

def get_no(text, str):
	offset = FindSubString(text, str)
	#print text[offset]
	for i in range((offset + 1), len(text)):
		if text[i] == '<':
			break
	#print text[offset+1 : i]
	number = int(text[offset+1 : i])
	print number
	return number 
	
def check_sefeweb_norton(link):
	url = 'https://safeweb.norton.com/report/show?url=' + link 
	print url
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	data = opener.open(url).read()
	soup = BeautifulSoup(data, 'lxml')
	text = soup.find_all('div', 'span10')
	print soup
	if "Computer Threats" in str(text[0]):
		Threat_cnt = get_no(str(text[0]), "Computer Threats")
	if "Annoyance factors" in str(text[0]):	
		factors_cnt = get_no(str(text[0]), "Annoyance factors")	
	if "Identity Threats" in str(text[0]):	
		Identity_Threats_cnt = get_no(str(text[0]), "Identity Threats")
		
	return Threat_cnt + factors_cnt + Identity_Threats_cnt
			

def main():
    #string = {'q': ' '.join(sys.argv[1:])}
    #string['q'] = '\"' + string['q'] + '\"'
	string = sys.argv[1]
	print string
	#return_status = check_siteadvisor(string)
	return_status = check_sefeweb_norton(string)
	print return_status
    #fd_malicious_links = open("malicious_link.txt", "r")
    #malicious_link = fd_malicious_links.readlines()

main()
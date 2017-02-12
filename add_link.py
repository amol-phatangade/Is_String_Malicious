import os, sys

def check_repetedlink(link, data):
    for i in data:
        if i[:-1] in link:
            print "Link is Allready Exist"
            return 0
        
    return 1


    
def main():

    fd = open("malicious_link.txt", "r")
    data = fd.readlines()
    if check_repetedlink(sys.argv[1], data) == 1:
        fd.close()
        fd = open("malicious_link.txt", "a")
        fd.write(sys.argv[1]+"\n")
        fd.close
    
        

main()
    


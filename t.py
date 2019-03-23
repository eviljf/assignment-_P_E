import requests
import webbrowser #not imported for any reason 
from bs4 import BeautifulSoup # where the magic happens

def datasaver(url_needed):
    request_variable=requests.get("https://en.wikipedia.org/"+ url_needed)
    file2save=open('file2save.html','wb')
    file2save.write(request_variable.content)




def gettingfiles():   #function to get files 
    f=open("newfile.html","w+")
    p=input("what do you want:")
    p=p.replace(' ','+')
    print (p)

    i=[]

    r=requests.get("https://en.wikipedia.org/w/index.php?search="+p+"&title=Special%3ASearch&go=Go")
    #r=requests.get("https://quicksoftwaretesting.com/sample-wsdl-urls-testing-soapui")#site i used to test
    p=r.content
    q=BeautifulSoup(p,'html.parser') #parsing using beautiful soup
    #f.write(q.find_all('a'))
    for z in q.find_all('a'):
        i.append(z.get("href"))

    for item in i:
        f.write("%s\n" % item)
    
    datasaver(i[20])




gettingfiles()






''' ----------Shitty P.E assignment (could be used)--------------'''
'''---made----by----that-one-guy-who-dosen,t-know-an-apostrophe-from-a-comma-----------'''
'''----this uses BeautifulSoup , for more info (https://beautiful-soup-4.readthedocs.io/en/latest)'''
import docx
from docx import Document
import requests
import webbrowser #not imported for any reason 
from bs4 import BeautifulSoup # where the magic happens
import re
'''---------------------vAriables-------------'''
document=Document()
'''---------------test condition-----'''
def test_er():
    f=open('file2save.html','rb')
    soup_er(f)



'''------------------------saves the data----------------------'''
def datasaver(url_needed):
    request_variable=requests.get("https://en.wikipedia.org/"+ url_needed)
    soupin_variable=request_variable.content
    file2save=open('file2save.html','wb')
    file2save.write(request_variable.content)
    #soup_er(request_variable)
'''------------The second souper---------------'''
def soup_er(soupin_variable):
    #soup_ed=BeautifulSoup(soupin_variable)
    soup = BeautifulSoup(soupin_variable)
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text=soup.get_text()
    doccex(visible_text)
'''-------------------------docx maker-----------'''
def doccex(visible_text):
    str_new=[]
    for line in visible_text:
        str_new.append(line)
    document.add_paragraph(str_new)
    document.save('test3.docx')
    refiner(str_new)
'''---------------------refiner-------------------'''
def refiner():
    kill_list=['']
    for line in str_new:
        






'''------------------------information extractor-------------------'''
#def info_extract(data_needed):

'''--------------------crawler------------------------'''
def crawler(var):
    for line in var:
        datasaver(var)




'''-----------------------gets the files--------------------------------'''
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
    
    #datasaver(i[20]) #Change the value here to get different urls returned in wikipedia search
    test_er()



test_er()






''' ----------Shitty P.E assignment (could be used)--------------'''
'''---made----by----that-one-guy-who-dosen,t-know-an-apostrophe-from-a-comma-----------'''
'''----this uses BeautifulSoup , for more info (https://beautiful-soup-4.readthedocs.io/en/latest)'''
import docx
from docx import Document
import requests
import webbrowser #not imported for any reason 
from bs4 import BeautifulSoup # where the magic happens
'''---------------------vAriables-------------'''
document=Document()
test_txt=open("test.txt","w")
test2_txt=open("test2.txt","w")
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
'''---------------------refiner-------------------'''
def refiner():
    t=0
    kill_list=['External links','^','Retrieved from "https','See also'] # This part is to remove the excess content in wikipedia
    delete_list = ["[edit]"]
    other_deathlist=["From Wikipedia, the free encyclopedia", "Jump to navigation", "Jump to search"]
    for line in str_new:
        
        if (kill_list[0] in line) or (kill_list[1] in line) :
            str_new.pop(t)
             
        elif(kill_list[2] in line) or (kill_list[3] in line) :
            death_var=death_var+1         
        elif (other_deathlist[0] in line) or (other_deathlist[1] in line) or (other_deathlist[2] in line ) :
            line.rstrip('\n')
        else:
            for word in delete_list:
                line = line.replace(word, "")
                fout.write(line)
        if death_var == 2:
            break
        t=t+1
        




'''------------------------information extractor-------------------'''
#def info_extract(data_needed):

'''--------------------crawler------------------------'''
def crawler(var):
    for line in var:
        datasaver(var)
'''----------------------link refiner------------------'''
def link_refiner(link_list):
    http_link='https://'
    http_links=[]
    ind_ex=0
    for line in link_list:
        if http_link in line:
            http_links.append(str(line))
            link_list.pop(ind_ex)
        elif line[0]=='#':
            link_list.pop(ind_ex)
        ind_ex=ind_ex+1
            

    for line in http_links:
        test_txt.write(line+"\n")
    for line in link_list:
        test2_txt.write(line+"\n")
        
        




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
    
    return(i)#datasaver(i[20]) #Change the value here to get different urls returned in wikipedia search
    #test_er()



link_list=gettingfiles()
link_no=0
lnk_str=[]
for line in link_list:
    print(str(line) + "\n"+str(link_no))
    lnk_str.append(str(line))
    link_no=link_no+1

link_refiner(lnk_str)#refines links






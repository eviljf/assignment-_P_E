from bs4 import BeautifulSoup

html = open('file2save.html','rb')
soup = BeautifulSoup(html)
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
print ("the type of the text" + str(type(visible_text)))
with open("finally_edited","w+") as f:
    for line in visible_text:
        try:
            f.write(line)
        except UnicodeEncodeError:
            pass


infile = "finally_edited"
outfile = "cleaned_file.txt"
kill_list=['^']
delete_list = ["[edit]"]
fin = open(infile,"r")
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
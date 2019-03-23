from bs4 import BeautifulSoup

html = open('file2save.html','rb')
soup = BeautifulSoup(html)
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
visible_text = soup.getText()
with open("finally_edited","w+") as f:
    f.write(visible_text)


infile = "finally_edited"
outfile = "cleaned_file.txt"
kill_list=['^']
delete_list = ["[edit]"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
    for word in kill_list:
        line.replace("")
fin.close()
fout.close()
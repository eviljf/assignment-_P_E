infile = "finally_edited"
outfile = "cleaned_file.txt"
kill_list=['External links','^']
delete_list = ["[edit]"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    if (kill_list[0] in line) or (kill_list[1] in line) :
        line.rstrip('\n')
    else:
        for word in delete_list:
            line = line.replace(word, "")
            fout.write(line)
        
        
           
    

        
        
fin.close()
fout.close()
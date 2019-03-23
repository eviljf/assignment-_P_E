infile = "finally_edited"
outfile = "cleaned_file.txt"
kill_list=['External links','^','Retrieved from "https','See also'] # This part is to remove the excess content in wikipedia
delete_list = ["[edit]"]
other_deathlist=["From Wikipedia, the free encyclopedia", "Jump to navigation", "Jump to search"]
fin = open(infile)
fout = open(outfile, "w+")
death_var=0
for line in fin:
    if (kill_list[0] in line) or (kill_list[1] in line) :
        line.rstrip('\n')
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
        
        
           
    

        
        
fin.close()
fout.close()
#junk between line 61 . 

with open(x, 'w',newline='') as wri:

        write_obj = csv.writer(wri)

        for i in range(len(namelis)):
            fields[0] = namelis[i]
            fields[1] = reciever_list[i]
            write_obj.writerow(fields)
        
    wri.close()
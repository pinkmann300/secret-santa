import csv
import random
from os import name
import smtplib
from email.message import EmailMessage
import os


def emailbaby(x, y, z, l):
    import csv
    import smtplib
    import ssl
    SUBJECT = "You are going to be the secret elf for....!!!"
    TEXT = """Hi {y}, 

    Firstly, thank you for signing up for the Secret Santa Gift Exchange! This Christmas you are going to be the Santa elf for {z}. Their address is {l}. Be sure to send your gift well in advance, as you know Santa is never late! 

    P.S. Happy Holidays :)

    Regards, 
    Rec Club"""
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)


    from_address = "sias.recreation@krea.ac.in"
    from_password = "ardmpcijejdgadiy"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_address, from_password)
        server.sendmail(
            from_address,
            x,
            message.format(y=y, z=z, l=l),
        )





def randomiser(x):

    namelis = []

    with open(x, 'r')as baby:
        namecon = csv.DictReader(baby)
        for row in baby:
            namelis.append(row[:-1])


    random.shuffle(namelis)

    print("Sender: ", namelis)

    print("\n")

    reciever_list = [' '] * len(namelis)

    for i in range(0,len(namelis)):

        if i != (len(namelis)-1):
            reciever_list[i] = namelis[i+1]

        else:
            reciever_list[i] = namelis[0]


    print("Reciever: ", reciever_list)
    print("\n")


    fields = [' '] * 2 

    with open(x, 'w', newline='') as wri:

        write_obj = csv.writer(wri)

        for i in range(len(namelis)):
            fields[0] = namelis[i]
            fields[1] = reciever_list[i]
            write_obj.writerow(fields)

    wri.close()


    print("\n")
    
    print(len(namelis))

    print("\n")
    

    def field_build(namelis, reciever_list):
        rel_em = []
        relev = []
        for i in range(0,len(namelis)):
            print(namelis[i])
            print("\n")
            sendmail_det = namelis[i].split('"')
            print(sendmail_det)
            rel_em = sendmail_det[0:(len(sendmail_det)-2)]
            namemail = rel_em[0].split(',')
            semail = namemail[0]
            print("Sendto email :", semail)
            fname_lis = namemail[1].split(' ')
            fname = fname_lis[0]
            print("Sendto Fname: ", fname)
            print("\n")
            reciever_det = reciever_list[i].split('"')
            relev = reciever_det[0:(len(reciever_det)-2)]
            recmail = relev[0].split(',')
            recmail = recmail[1]
            print("Reciever Name: ",recmail)
            add = reciever_det[(len(sendmail_det)-2)]
            print("Reciever address: ", add)
            print("\n")
            emailbaby(semail,fname,recmail,add)

    field_build(namelis,reciever_list)


randomiser('secsan23no.csv')
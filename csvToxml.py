#--coding: utf-8-
import csv
import os
import codecs
path_dir = './done/'
file_list = os.listdir(path_dir)
code = 1
filename = open('output.txt','w',encoding='euc-kr')

for file in file_list:
    if(file.endswith(".csv")):
        print(file)
        filepath=path_dir+file
        print(filepath)
        with open(filepath,'r',encoding='euc-kr',errors='ignore') as csvfile:
            reader =csv.reader(csvfile)

            for row in reader:
                #print(row[0],row[1],row[2],row[3])
                row0=str(row[0])
                if(row0.startswith("병명")or row0 is ''):
                    continue
                row0=row0.replace("\n","")
                row1=str(row[2])
                row2=str(row[1])
                row3=str(row[3])
                row1=row1.replace("\n","")
                row2 = row2.replace("\n", "")
                row3 = row3.replace("\n", "")
                filename.write("{code : "+str(code)+',\n'
                            +'name : '+"'"+row0+"'"+",\n"
                            +'cause :'+"'"+row1+"',\n"
                            +'symptom :'+"'"+row2+"',\n"
                            +'part  :'+"'"+row3+"',\n"
                            +'desc  :},\n'
                               )
                code+=1
    else:
        continue;

filename.close()
import csv
import itertools
import os
path_dir = './texts/'
file_list = os.listdir(path_dir)
for file in file_list:
    print(file)
    name=file.split('.')[0]
    csvfile = open(path_dir+name+".csv","w")
    writer = csv.writer(csvfile)
    writer.writerow(('병명','증상','원인'))
    one=""
    two=""
    three=""
    with open(path_dir+file,'r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
            if(line.startswith("*")):
                line = line.replace("*"," ")
                one=line
            elif(line.startswith("2.")):
                line=line.replace("2."," ")
                two=line
            elif(line.startswith("3.")):
                line = line.replace("3."," ")
                three=line
                writer.writerow((one,two,three))
                one=two=three=""
        f.close()
    csvfile.close()

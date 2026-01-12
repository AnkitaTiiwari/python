#we're removing headers from files

#loop through files in current directory
import os,pathlib,csv

folder = os.getcwd() + '/RemoveHeader'
new_folder = os.chdir(path= folder)
#print(new_folder)


for filename in os.listdir(new_folder):
    csvUpdatedData = []
    #print(filename)
    if filename.endswith('.csv'):
        #print(filename)
        csvFileName = open(filename)
        csvData = csv.reader(csvFileName)
        for rows in csvData:
            print(rows)
            if csvData.line_num == 1:
                continue
            csvUpdatedData.append(rows)
        csvFileName.close()

    #write updated data to new csv file
        csvFileNew = open('removed/' + filename,'w',newline='')
        csvWriter = csv.writer(csvFileNew)
        for row in csvUpdatedData:
            csvWriter.writerow(row)
        csvFileNew.close()  

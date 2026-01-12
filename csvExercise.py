import csv

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)

#can read in list and access via [row][col]
# exampleData = list(exampleReader)
# #print(exampleData)
# print(exampleData[0][0])
# print(exampleData[2][1])

#can loop through
# for row in exampleReader:
#     print('Row # '+ str(exampleReader.line_num) + ' ' + str(row[0]) )

#writing things to csv
# outputFile = open('output.csv','w',newline='')
# outputWriter = csv.writer(outputFile,delimiter='\t',lineterminator='\n\n')
# outputWriter.writerow(['Spam','eggs','bacon','ham'])
# outputWriter.writerow(['Hello,world!','eggs','bacon','ham'])
# outputFile.close()

#DictReader and DictWriter
# exampleFile = open('exampleWithHeader.csv')
# exDictReader = csv.DictReader(exampleFile)
# for row in exDictReader:
#     print(row['Timestamp'],row['Fruit'],row['Quantity'])

# outputFile = open('example.csv')
# outputDict = csv.DictReader(outputFile,['Timestamp','Fruit','Quantity'])
# for row in outputDict:
#     print(row['Timestamp'])
#     print(row['Fruit'])

#writin into csv with dict
dictWritingFile = open('FileWithHeader.csv','w',newline='')
dictWritingWrite = csv.DictWriter(dictWritingFile,['Name','Place'])
dictWritingWrite.writeheader()
dictWritingWrite.writerow({'Name':'Kimi','Place':'Pendra'})
dictWritingFile.close()
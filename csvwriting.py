#import module
import csv
#create file
csvfile = open('csvwriting.csv', 'w')
#create csvwriter
csvwriter = csv.writer(csvfile, delimiter=',')
#write information
csvwriter.writerow(["hi friends", "How are you?"])
#close file
csvfile.close() 
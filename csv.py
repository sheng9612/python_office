# write CSV
import csv

outputFile = open('output.csv','w',newline = '')

outputwriter = csv.writer(outputFile)

outputwriter.writerow(['spam','eggs','bacon','ham'])

outputwriter.writerow(['Hellom, World', 'eggs', ' bacon', 'ham
                       '])

outputwriter.writerow([1,2,3.131414,4])

outputFile.close()

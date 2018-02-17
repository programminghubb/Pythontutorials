#importing CSV module 
import csv
# Creating  or opening csv file with write mode
with open('newcsvfile.csv', 'w') as csvfile:
    # Calling inbuilt write method of csv module 
    csv_writer = csv.writer(csvfile, delimiter=',')
   # Calling writerow method to iterate over passed values
    csv_writer.writerow([ 'Name', 'Address', 'Roll' ])
    csv_writer.writerow([ 'Programming', 'Hub', '1' ])
    csv_writer.writerow([ 'Python', 'Program', '2' ])
    csv_writer.writerow([ 'Open', 'Source', '3' ])

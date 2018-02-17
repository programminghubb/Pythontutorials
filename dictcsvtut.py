import csv
with open('newcsvfile.csv', 'r') as csvfile:
    # Calling DictReader object to read csv file
    csvreader = csv.DictReader(csvfile)
    with open('newentry.csv', 'w') as newentry:
        # defining fieldnames
        fieldnames = [ 'Name', 'Address' ]
        # Calling DictWriter object to write csv file
        csvwriter = csv.DictWriter(newentry, fieldnames=fieldnames, delimiter='|')
       #  writing header which writes fields names as header in first row
        csvwriter.writeheader()
        for line in csvreader:
            # deleting all Roll data to create new csv file
            del line[ 'Roll' ]
             # writing data to newentry.csv after deleting Roll
            csvwriter.writerow(line)

import csv

with open('Tokyo Medals 2021.csv', 'r') as medals_file:
    spreadsheet = csv.DictReader(medals_file)
    for row in spreadsheet:
        print(row['Country'], row['Gold Medal'])

import csv

with open('definitions.csv', 'a') as csvfile:
    fieldnames = ['word', 'definition']
    dictionary_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    dictionary_writer.writeheader()
    dictionary_writer.writerow({
        'word': 'Antipathy',
        'definition': 'Deep dislike, sometimes without reason.'
        })

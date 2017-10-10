import csv

with open('/Users/lawerencelee/py_tech_degree/no_data.csv', newline='') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',')
    rows = list(my_reader)
    for row in rows[:]:
        print(row)

    # my_reader = csv.DictReader(csvfile, delimiter=',', )
    # rows = list(my_reader)
    # for row in rows[0:]:
    #  	print(row['humidity'])

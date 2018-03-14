import csv

inventoryMain = raw_input("Input path to main CSV: ")
inventoryCompare = raw_input("Input path to comparison CSV: ")

mainCSV = csv.DictReader(open(inventoryMain, 'rU'))
compareCSV = csv.DictReader(open(inventoryCompare, 'rU'))

csv_one = []
csv_two = []
wrong = []

for item in compareCSV:
    csv_one.append(item)

for item in mainCSV:
    csv_two.append(item)

error_count = 0

ref_column = raw_input("Input a reference column header (must be the same in both CSVs):")
compare_column = raw_input("Input a column heading you would like to compare (must be the same in both CSVs):")
title_column = raw_input("Input a title column header (must be the same in both CSVs):")

print

for item in csv_one:
    for i in csv_two:
        if item[ref_column] == i[ref_column]:
            if item[compare_column] != i[compare_column]:
                print "Item %s: " % (item[title_column] + ' ' + item[ref_column]) + item[compare_column] + " not " + i[compare_column]
                wrong.append({'Compare title' : item[title_column], 'Compare Sku' : item[ref_column], 'Compare Stock' : item[compare_column],
                              'Main title' : i[title_column], 'Main Sku' : i[ref_column], 'Main Stock' : i[compare_column]})
                error_count+=1

print

if error_count > 1:
    print "%s errors" % error_count
else:
    print "1 error"

print
print "See wrong_items.csv for details."
print

colHeaders = ['Compare title', 'Compare Sku', 'Compare Stock',
              'Main title', 'Main Sku', 'Main Stock']

with open('wrong_items.csv', 'w') as wrongfile:
    writer = csv.DictWriter(wrongfile, fieldnames=colHeaders)
    writer.writeheader()
    for item in wrong:
        writer.writerow(item)
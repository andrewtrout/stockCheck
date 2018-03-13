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

print

error_count = 0

for item in csv_one:
    for i in csv_two:
        if item['Sku'] == i['Sku']:
            if item['Stock'] != i['Stock']:
                print "Stock of %s: " % (item['Name'] + ' ' + item['Sku']) + item['Stock'] + " not " + i['Stock']
                wrong.append({'Compare title' : item['Name'], 'Compare Sku' : item['Sku'], 'Compare Stock' : item['Stock'],
                              'Main title' : i['Name'], 'Main Sku' : i['Sku'], 'Main Stock' : i['Stock']})
                error_count+=1

print
print "%s errors" % error_count
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
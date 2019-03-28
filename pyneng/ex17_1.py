import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]

with open('test.csv', 'w') as w:
#with open('test.csv', 'w') as w, open('querry.csv') as f:
	#reader = csv.reader(f)
    writer = csv.writer(w)

    for row in data:
    	writer.writerow(row)

import csv
field_names=['REGNUMBER','NAME','COURSE']

data=[{'REGNUMBER':101,'NAME':'Ananya','COURSE':'MCA'},{'REGNUMBER':102,'NAME':'Sindoori','COURSE':'MCA'},{'REGNUMBER':103,'NAME':'Nourin','COURSE':'MCA'}]
with open('Details.csv','w', newline='')as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(data)


with open('Details.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

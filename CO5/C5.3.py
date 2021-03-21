import csv
with open('Cars.csv','w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["SN","Carname","Rating"])
    writer.writerow([1,"Ford",6])
    writer.writerow([2,"Terrano",7])
    writer.writerow([3,"XUV",4])

with open('Cars.csv')as csvfile:
    data=csv.reader(csvfile)
    for row in data:
        print(','.join(row))

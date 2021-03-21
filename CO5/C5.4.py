import csv
with open("Bikes.csv",'w',newline='') as file:
  write=csv.writer(file)
  write.writerow(["Sl.No","Bikes\n","Rating"])
  write.writerow(["1","Royal Enfield","8"])
  write.writerow(["2","Splender","5"])
  write.writerow(["3","Hero Hunk","6"])
  write.writerow(["4","YamahaR15","7"])
  
with open("Bikes.csv" ,'r') as file:
    data=csv.reader(file)
    print("Contents in Column 'Bikes': ")
    for r in data:
        print(r[1])

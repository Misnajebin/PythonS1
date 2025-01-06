import csv 

file1=open("data.csv","r",newline='')
# csv_r=csv.writer(file1)
# lis=["misna","afraq","Mammu"]
# csv_r.writerow(lis)

csv_read=csv.reader(file1)
cs=list(csv_read)
print(cs)
for row in csv_read:
    print(row)
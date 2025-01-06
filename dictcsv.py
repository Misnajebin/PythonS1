file1=open("data.csv","w+")
dict={1:"mammu",5:"misna",7:"Zuhri"}
for key in dict.keys():
    file1.write(dict[key])


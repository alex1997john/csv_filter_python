import csv

d={}
reader = csv.DictReader(open("output/filteredCountry.csv"))
for raw in reader:
    if raw['SKU'] in d.keys():
        if d[raw['SKU']][1] == d[raw['SKU']][2]:
            d[raw['SKU']].pop()
            d[raw['SKU']].append(raw['PRICE'])
    else:
        a=raw['SKU']
        b=raw['PRICE']
        d[raw['SKU']]=[a,b,b]
# for i in d:
#     if len(d[i])==2:
#         d[i].append(d[i][1])
a=[]
for i in d:
    a.append(d[i])
with open('output/lowestPrice.csv','w',newline='') as f:
    header=['SKU','FIRST_MINIMUM_PRICE', 'SECOND_MINIMUM_PRICE']
    write = csv.writer(f)
    write.writerow(header)
    write.writerows(a)
print('successfull')
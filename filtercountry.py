import csv
from re import search
names=[]
reader = csv.DictReader(open("input/main.csv"))
for raw in reader:
    if raw['COUNTRY'].find('USA')!=-1:
        names.append({
           'SKU':raw['SKU'],
            'DESCRIPTION':raw['DESCRIPTION'],
            'YEAR':raw['YEAR'],
            'CAPACITY':raw['CAPACITY'],
            'URL':raw['URL'],
            'PRICE':raw['PRICE'],
            'SELLER_INFORMATION':raw['SELLER_INFORMATION'],
            'OFFER_DESCRIPTION':raw['OFFER_DESCRIPTION'],
            'COUNTRY':raw['COUNTRY']
        }
        )
with open('output/filteredCountry.csv','w',newline='') as file:

    header=['SKU','DESCRIPTION','YEAR','CAPACITY','URL','PRICE','SELLER_INFORMATION','OFFER_DESCRIPTION','COUNTRY']
    csv_dict_writer = csv.DictWriter(file, fieldnames=header)
    csv_dict_writer.writeheader()
    for i in names:
        csv_dict_writer.writerow(i)


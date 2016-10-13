import csv

def main():
    ETC = open('../Datasets/ETC.csv', "rb")
    reader = csv.reader(ETC)
    for i, row in enumerate(reader):
        if i==0: continue
        code = row[0]
        orgs = row[4]
        orgs = orgs.split(",")
        for organization in orgs:
            concatenated = code + "_" + organization
            print(concatenated)
main()
    

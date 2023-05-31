import pandas as pd
import csv

read_file = pd.read_excel ("test.xlsx")


read_file.to_csv ("test.csv",
				index = None,
				header=True)


df = pd.DataFrame(pd.read_csv("test.csv"))


with open('test.csv', newline='') as in_file:
    with open('test_refactored.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(row):
                writer.writerow(row)

df



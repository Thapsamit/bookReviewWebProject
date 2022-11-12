import MySQLdb
import csv
mydb = MySQLdb.connect(host="localhost", user="root",
                       password="78520", database="bookreview")

with open("books.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter=",")
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3])
        all_value.append(value)

query = "insert into books(isbn,title,author,year) values (%s,%s,%s,%s)"
mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()

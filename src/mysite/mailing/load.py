import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='regusers')
cursor = mydb.cursor()

csv_data = csv.reader(file('reg_users.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO testcsv(name, \
          email)' \
          'VALUES("%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
#print "Done"
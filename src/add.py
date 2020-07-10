import xlrd
import pymysql

#Store file in book
book = xlrd.open_workbook("data.xls")
sheet = book.sheet_by_name("Sheet1")
#print(sheet.cell(2,3).value)

database = pymysql.connect (host="localhost", user = "root", passwd = "password", db = "consumption")
cursor = database.cursor()
query = """INSERT INTO final (Sno, RecDate, old_qtr, ananda_nivas, budha_nivas, palash, kadamb, parijaat, bakul, sahana_aithi_house, nilgiri, vindhya, admin_block, krb, bodh, total_in_kl, type_of_reading) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
for r in range(2, 1141):
	Sno = sheet.cell(r,0).value
	RecDate = sheet.cell(r,1).value
	old_qtr = sheet.cell(r,2).value
	ananda_nivas = sheet.cell(r,3).value
	budha_nivas = sheet.cell(r,4).value
	palash = sheet.cell(r,5).value
	kadamb = sheet.cell(r,6).value
	parijaat = sheet.cell(r,7).value
	bakul = sheet.cell(r,8).value
	sahana_aithi_house = sheet.cell(r,9).value
	nilgiri = sheet.cell(r,10).value
	vindhya = sheet.cell(r,11).value
	admin_block = sheet.cell(r,12).value
	krb = sheet.cell(r,13).value
	bodh = sheet.cell(r,14).value
	total_in_kl = sheet.cell(r,15).value
	type_of_reading = sheet.cell(r,16).value
	values = (Sno, RecDate, old_qtr, ananda_nivas, budha_nivas, palash, kadamb, parijaat, bakul, sahana_aithi_house, nilgiri, vindhya, admin_block, krb, bodh, total_in_kl, type_of_reading)
	cursor.execute(query, values)

cursor.close()
database.commit()
database.close()

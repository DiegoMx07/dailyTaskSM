import os, time, datetime

#1.- Revisar backups base de datos en Servidor de SV (completo, diferencial y TCA)
backFile  = ['TCADBPAD_Dif1.bkf', 'TCADBPAD_Dif2.bkf', 'TCADBPAD.bkf', 'TCADBTCA.bkf']
location  = '//fipa2sv/d$/Temp/Backup/'

while True:
	try:
		for i in range(len(backFile)):

				dateFile  = datetime.datetime.strptime(time.ctime(os.path.getmtime(location+backFile[i])), "%a %b %d %H:%M:%S %Y").date()
				print("El último respaldo del archivo " + backFile[i] + " fue el día:")
				print(dateFile)
				if (dateFile==datetime.date.today()):
					print("El respaldo se ejecutó de manera correcta")
				else:
					print("El respaldo no se ejecutó")
				input()
		break
	except ValueError:
			print("ValueError")



#2.-Revisar backups base de datos en Servidor de APP (completo, diferenciales y TCA) 



"""
backFile  = ['TCADBPAD_Dif1.bkf', 'TCADBPAD_Dif2.bkf', 'TCADBPAD.bkf', 'TCADBTCA.bkf']
location  = '//fipa2app/d$/Temp/Backup/'



for i in range(len(backFile)):

		dateFile  = datetime.datetime.strptime(time.ctime(os.path.getmtime(location+backFile[i])), "%a %b %d %H:%M:%S %Y").date()
		print(dateFile==datetime.date.today())

"""




"""
#3.- Revisar backup a cinta

#location = '//fipa2app/G$/'
location  = '//fipa2sv/d$/WSUS/'
#folder   = 'Backup'
folder	  = 'WsusContent'

dateFile = datetime.datetime.strptime(time.ctime(os.path.getmtime(location+folder)), "%a %b %d %H:%M:%S %Y").date()
print (dateFile)

"""
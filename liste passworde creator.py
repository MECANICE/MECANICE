mport random  ,time,os
char=("abcdefghijklmnopqrstuvwxyz")
list=[]
activate=1
while activate:
	passworde=random.choice(char)
	if passworde not in list:
		list.append(passworde)
		time.sleep(1)
		print(list)
	else:
		time.sleep(1)
		print("## : ",passworde)
		pass
		
	if len(list)==26:
		os.system("clear")
		print("======================== world Liste =======================")
		print(list)
		break

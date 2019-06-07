import random
from admin import *
from dbSQL import *

# 主菜单
# 选择预定/查询/取消预定
def mainMenu():
	print("+------------TourBookingSystem------------+")
	print("|  1.预定航班/大巴车/宾馆房间             |")
	print("|  2.查询航班/大巴车/宾馆房间预定信息     |")
	print("|  3.取消航班/大巴车/宾馆房间预定         |")
	print("|  4.查询旅行线路                         |")
	print("|  5.检查线路合理性                       |")
	print("|  0.退出                                 |")
	print("+-------------CustomerService-------------+")
	choice = input("请选择服务(0/1/2/3/4/5):")
	if choice in ["1","2","3","4","5","0"]:
		return int(choice)
	else:
		print("请重新输入")
		return mainMenu()

# 内菜单
# 选择航班/酒店/大巴
def inMenu(str):
	choice = input("1.%s航班 2.%s大巴车 3.%s宾馆房间:" % (str, str, str))
	if choice in ["1","2","3"]:
		return int(choice)
	else:
		print("请重新输入")
		return inMenu(str)

# 检查custID是否在数据库内
# ID为空时返回全部custID
def queryCustomer(ID):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	
	sql = "select custID from CUSTOMERS where custID = '%s'" % (ID)
	if ID=="" :
		sql = "select custID from CUSTOMERS"

	custs = []
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		result = cursor.fetchall();
		for row in result:
			custs.append(row[0])
	except:
		pass
	# 关闭数据库连接
	db.close()
	return custs

# 插入新的用户
# 成功返回True, 失败返回False
def insertCustomer(ID, name):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	sql = "insert into CUSTOMERS values('%s', '%s')" % (ID, name)
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
		# 关闭数据库连接
		db.close()
		return True
	except:
		# 如果发生错误则回滚
		db.rollback()
		db.close()
		return False

# 查询RESERVATIONS表
def queryReserv(ID):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	sql = ""
	if ID == "":
		sql = "select * from RESERVATIONS"
	else:
		sql = "select * from RESERVATIONS where ID = '%s'" % (ID)

	resvs = []
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		result = cursor.fetchall();
		for row in result:
			resvNum = row[0] #, row[1], row[2], row[3], row[4], row[5]
			resvs.append(resvNum)
			#print("%9s %5d %8d %8d %8s %8s" % (flightNum, price, numSeats, numAvail, FromCity, ArivCity))
	except:
		print("Error!")
	# 关闭数据库连接
	db.close()
	return resvs

# 插入RESERVATIONS表
def insertReserv(ID, resvType, resvKey):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	resvNum = str(random.randint(1, 100000))
	while resvNum in queryReserv(""):
		resvNum = str(random.randint(1, 100000))

	sql = "insert into RESERVATIONS values('%s', '%s', %d, '%s')" % (resvNum, ID, resvType, resvKey)
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
		db.close()
		return True
	except:
		# 如果发生错误则回滚
		db.rollback()
		db.close()
		return False

# 用户预定
def CustomerService1(ID):
	ch2 = inMenu("预定")
	# 预定航班
	if ch2==1:
		sql = "select * from FLIGHTS"
		try:
			FromCity, ArivCity = input("请输入出发/抵达城市(FromCity ArivCity):").split(" ")
			if FromCity!="" and ArivCity!="" :
				sql = "select * from FLIGHTS where FromCity = '%s' and ArivCity = '%s'" % (FromCity, ArivCity)
		except:
			print("输入格式有误,将查询全部航班")
			FromCity, ArivCity = "", ""
		# 查询航班
		flights = exctQuerySQL(sql)
		if len(flights)==0 :
			print("很抱歉，没有您想要的航班")
		else :
			# 显示航班信息
			print("所有航班信息如下:")
			print(FORMAT_FLIGHTS)
			for each in flights :
				print(each)
			# 预定航班
			flightNum = "-1"
			flightNums = [x[0] for x in flights]
			while flightNum not in flightNums:
				flightNum = input("请选择航班编号(输入0取消):")
				if flightNum=="0":
					break
			# 确认		
			if flightNum!="0" :
				dec = input("是否选择航班 %s ?(Y/N):" % (flightNum))
				if dec=="Y" or dec=="y" :
					insertReserv(ID, 1, flightNum)
					print("预定成功!")
				elif dec=="N" or dec=="n" :
					print("操作已取消，感谢您的使用")
			
	# 预定大巴车
	elif ch2==2:
		City = ""
		try:
			City = input("请输入城市:")
		except:
			print("输入为空,将查询全部大巴车")
			City = ""
		# 查询大巴车
		querySQL = "select * from BUS where location = '%s'" % (City)
		buses = exctQuerySQL(querySQL)
		if len(buses)==0 :
			print("很抱歉，没有您想要的大巴车")
		else :
			# 显示大巴车信息
			print("所有大巴车信息如下:")
			print(FORMAT_BUS)
			for each in buses :
				print(each)

			# 预定大巴车
			busNum = "-1"
			busNums = [x[0] for x in buses]
			while busNum not in busNums:
				busNum = input("请选择大巴车编号(输入0取消):")
				if busNum=="0":
					break
			# 确认		
			if busNum!="0" :
				dec = input("是否选择大巴车 %s ?(Y/N):" % (busNum))
				if dec=="Y" or dec=="y" :
					insertReserv(ID, 3, busNum)
					print("预定成功!")
				elif dec=="N" or dec=="n" :
					print("操作已取消，感谢您的使用")

	# 预定宾馆
	else:
		City = input("请输入城市:")
		# 查询宾馆
		querySQL = "select * from HOTELS where location = '%s'" % (City)
		hotels = exctQuerySQL(querySQL)
		if len(hotels)==0 :
			print("很抱歉，没有您想要的宾馆")
		else :
			# 显示宾馆信息
			print("所有宾馆信息如下:")
			print(FORMAT_HOTELS)
			for each in hotels :
				print(each)
			# 预定宾馆
			hotelNum = "-1"
			hotelNums = [x[0] for x in hotels]
			while hotelNum not in hotelNums:
				hotelNum = input("请选择宾馆编号(输入0取消):")
				if hotelNum=="0":
					print("操作取消，感谢您的使用")
					break
			# 确认		
			if hotelNum!="0" :
				dec = input("是否选择宾馆 %s ?(Y/N):" % (hotelNum))
				if dec=="Y" or dec=="y" :
					insertReserv(ID, 2, hotelNum)
					print("预定成功!")
				elif dec=="N" or dec=="n" :
					print("操作已取消，感谢您的使用")
	print("----------预定End----------\n")

# 查询  
# 根据ID查询全部预定信息		
def CustomerService2(ID):
	ch2 = inMenu("查询预定")
	# 查询航班预定信息
	if ch2==1:
		querySQL = "select %s \
					from RESERVATIONS natural join CUSTOMERS, FLIGHTS \
					where resvKey = flightNum and resvType = 1 and custID = '%s'" % (FORMAT+", FromCity, ArivCity", ID)
		flights = exctQuerySQL(querySQL)
		if len(flights)==0 :
			print("您没有预定任何航班")
		else :
			# 显示航班信息
			print("所有预定航班信息如下:")
			print("custName, custID, resvNum, flightNum, price, FromCity, ArivCity")
			for each in flights :
				print(each)

	# 查询大巴车预定信息
	elif ch2==2:
		querySQL = "select %s \
					from RESERVATIONS natural join CUSTOMERS, BUS \
					where resvKey = busNum and resvType = 3 and custID = '%s'" % (FORMAT+", location", ID)
		buses = exctQuerySQL(querySQL)
		if len(buses)==0 :
			print("您没有预定任何大巴车")
		else :
			# 显示大巴车信息
			print("所有预定大巴车信息如下:")
			print("custName, custID, resvNum, busNum, price, location")
			for each in buses :
				print(each)
		
	# 查询宾馆预定信息
	else:
		querySQL = "select %s \
					from RESERVATIONS natural join CUSTOMERS, HOTELS \
					where resvKey = hotelNum and resvType = 2 and custID = '%s'" % (FORMAT+", location", ID)
		hotels = exctQuerySQL(querySQL)
		if len(hotels)==0 :
			print("您没有预定任何宾馆")
		else :
			# 显示宾馆信息
			print("所有预定宾馆信息如下:")
			print("custName, custID, resvNum, hotelNum, price, location")
			for each in hotels :
				print(each)
	print("----------查询End----------\n")	

# 取消
# 根据resvNum取消相应预定信息
def CustomerService3(ID):
	ch2 = inMenu("取消预定")	
	resvNum = input("请输入预定编号:")
	# 取消预定航班
	if ch2==1:
		while True :
			sql = "select %s \
					from RESERVATIONS natural join CUSTOMERS, FLIGHTS \
					where resvKey = flightNum and resvType = 1 and resvNum = '%s'" % (FORMAT+", FromCity, ArivCity", resvNum)
			# 查询航班
			flight = exctQuerySQL(sql)
			if flight :
				# 显示航班信息
				print("查询的航班信息如下:")
				print(flight)

				cancel= input("是否取消预定(Y/N):")
				if cancel=="Y" or cancel=="y" :
					exctDeleteSQL("delete from RESERVATIONS where resvNum = '%s'" % (resvNum))
					print("已取消预定航班")
				elif cancel=="N" or cancel=="n" :
					print("操作已取消，感谢您的使用")
				break
			else :
				resvNum=input("很抱歉,没有预定信息,请重新输入编号(输入0取消):")
				if resvNum=="0" :
					break

	# 取消预定大巴车
	elif ch2==2:
		while True :
			sql = "select %s \
					from RESERVATIONS natural join CUSTOMERS, BUS \
					where resvKey = busNum and resvType = 3 and resvNum = '%s'" % (FORMAT+", location", resvNum)
			# 查询大巴车
			bus = exctQuerySQL(sql)
			if bus :
				# 显示大巴车信息
				print("查询的大巴车信息如下:")
				print(bus)
				cancel= input("是否取消预定(Y/N):")
				if cancel=="Y" or cancel=="y" :
					exctDeleteSQL("delete from RESERVATIONS where resvNum = '%s'" % (resvNum))
					print("已取消预定大巴车")
				elif cancel=="N" or cancel=="n" :
					print("操作已取消，感谢您的使用")
				break
			else :
				resvNum=input("很抱歉,没有预定信息,请重新输入编号(输入0取消):")
				if resvNum=="0" :
					break

	# 取消预定宾馆
	else:
		while True :
			sql = "select %s \
					from RESERVATIONS natural join CUSTOMERS, HOTELS \
					where resvKey = hotelNum and resvType = 2 and resvNum = '%s'" % (FORMAT+", location", resvNum)
			# 查询宾馆
			hotel = exctQuerySQL(sql)
			if hotel :
				# 显示宾馆信息
				print("查询的宾馆信息如下:")
				print(hotel)

				cancel= input("是否取消预定(Y/N):")
				if cancel=="Y" or cancel=="y" :
					exctDeleteSQL("delete from RESERVATIONS where resvNum = '%s'" % (resvNum))
					print("已取消预定宾馆")
				elif cancel=="N" or cancel=="n" :
					print("操作已取消，感谢您的使用")
				break
			else :
				resvNum=input("很抱歉,没有预定信息,请重新输入编号(输入0取消):")
				if resvNum=="0" :
					break
	print("----------取消End----------\n")

# 查询某个客户的旅行线路
def CustomerService4(ID):
	# 查询航班预定信息
	querySQL = "select %s \
				from RESERVATIONS natural join CUSTOMERS, FLIGHTS \
				where resvKey = flightNum and resvType = 1 and custID = '%s'" % (FORMAT+", FromCity, ArivCity", ID)
	flights = exctQuerySQL(querySQL)
	if len(flights) :
		# 获取航班信息
		for each in flights :
			FromCity, ArivCity = each[5], each[6]
			print("%s -> %s" % (FromCity, ArivCity))
	else :
		print("您未预定航班")
	print("----------线路End----------\n")	

# 检查线路合理性
def CustomerService5(ID):
	# 查询航班预定信息
	flag = False
	querySQL = "select %s \
				from RESERVATIONS natural join CUSTOMERS, FLIGHTS \
				where resvKey = flightNum and resvType = 1 and custID = '%s'" % (FORMAT+", FromCity, ArivCity", ID)
	flights = exctQuerySQL(querySQL)
	cities = []
	if len(flights) :
		# 显示航班信息
		# print("custName, custID, resvNum, flightNum, price, FromCity, ArivCity")
		for each in flights :
			cities.append(each[5])
			cities.append(each[6])
	else :
		print("您未预定航班")
		return

	# 查询大巴车预定信息
	querySQL = "select %s \
				from RESERVATIONS natural join CUSTOMERS, BUS \
				where resvKey = busNum and resvType = 3 and custID = '%s'" % (FORMAT+", location", ID)
	buses = exctQuerySQL(querySQL)
	if len(buses) :
		# 获取大巴车所在城市
		for each in buses :
			if each[5] not in cities:
				print("您的旅行线路不合理")
				return
	else :
		print("您未预定大巴车")
		return

	# 查询宾馆预定信息
	querySQL = "select %s \
				from RESERVATIONS natural join CUSTOMERS, HOTELS \
				where resvKey = hotelNum and resvType = 2 and custID = '%s'" % (FORMAT+", location", ID)
	hotels = exctQuerySQL(querySQL)
	if len(hotels) :
		# 获取宾馆所在城市
		for each in hotels :
			if each[5] not in cities:
				print("您的旅行线路不合理")
				return
	else :
		print("您未预定宾馆")
		return

	print("您的旅行线路合理")

# 函数入口
def Main():
	while True :
		print("------------------Welcome------------------")
		ID = input("请输入ID:")
		# 系统管理员
		if ID=="admin" :
			while True :
				ch1 = Menu()
				# 退出管理系统
				if ch1==0:
					print("---------------已退出管理系统--------------\n")
					break
				elif ch1==5:
					while True:
						print("Please input MySQL instructors in ONE line(Input exit to quit)")
						command = input()
						if command=="exit":
							break
						if exctSQL(command):
							print("成功执行")
						else:
							print("执行失败")
					break

				# 增删查改
				choice = input("1.Insert 2.Delete 3.Query 4.Modify 0.Back\n")
				if choice=="1":
					# 添加航班/大巴/宾馆/客户
					Insert(ch1)
				elif choice=="2":
					# 删除航班/大巴/宾馆/客户
					Delete(ch1)
				elif choice=="3":
					# 查询航班/大巴/宾馆/客户
					Query(ch1)
				elif choice=="4":
					# 修改航班/大巴/宾馆/客户
					print("暂未开放")
				else :
					pass
				
		# 退出
		elif ID=="exit" :
			break

		# 用户端服务
		else :
			if ID not in queryCustomer(ID):
				print("欢迎新客户使用本系统")
				name = input("您的姓名：")
				if insertCustomer(ID, name) :
					print("您的信息已登记")
			
			while True:
				ch1 = mainMenu()
				# 选择预定/查询/取消预定
				if ch1==1 :
					CustomerService1(ID)
				elif ch1==2 :
					CustomerService2(ID)
				elif ch1==3 :
					CustomerService3(ID)
				elif ch1==4 :
					CustomerService4(ID)
				elif ch1==5 :
					CustomerService5(ID)
				else :
					print("---------------已退出用户服务--------------\n")
					break

# 运行Main函数
Main()

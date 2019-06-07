from dbSQL import *

def Menu():
	print("+------------TourBookingSystem------------+")
	print("| 1.FLIGHTS  2.BUS  3.HOTELS  4.CUSTOMERS |")
	print("| 5.Command  0.Quit                       |")
	print("+--------------Administrator--------------+")
	choice = input("请选择服务(0/1/2/3/5):")
	if choice in ["1","2","3","4","5","0"]:
		return int(choice)
	else:
		print("请重新输入")
		return Menu()

# 插入
def Insert(ch1):
	#  插入航班
	if ch1==1:
		flightNum, price, numSeats, FromCity, ArivCity = input("请输入增加的航班信息(flightNum price numSeats FromCity ArivCity):").split(" ")
		sql = "insert into FLIGHTS values('%s', %d, %d, %d, '%s', '%s')" % (flightNum, int(price), int(numSeats), int(numSeats), FromCity, ArivCity)
	# 插入大巴
	elif ch1==2:
		busNum, location, price, numSeats = input("请输入增加的大巴车信息(busNum location price numSeats):").split(" ")
		sql = "insert into BUS values('%s', '%s', %d, %d, %d)" % (busNum, location, int(price), int(numSeats), int(numSeats))
	# 插入宾馆
	elif ch1==3:
		hotelNum, location, price, numRooms = input("请输入增加的宾馆信息(hotelNum location price numRooms):").split(" ")
		sql = "insert into HOTELS values('%s', '%s', %d, %d, %d)" % (hotelNum, location, int(price), int(numRooms), int(numRooms))
	# 插入客户
	else:
		custID, custName = input("请输入增加的客户信息(custID custName):").split(" ")
		sql = "insert into HOTELS values('%s', '%s')" % (custID, custName)

	if exctInsertSQL(sql):
		print("插入成功")
	else :
		print("插入失败")

# 删除
def Delete(ch1):
	sql = ""
	#  删除航班
	if ch1==1:
		flightNum = input("请输入删除的航班编号(flightNum):")
		sql = "delete from FLIGHTS where flightNum = '%s'" % (flightNum)
	# 删除大巴
	elif ch1==2:
		busNum = input("请输入删除的大巴编号(busNum):")
		sql = "delete from BUS where busNum = '%s'" % (busNum)
	# 删除宾馆
	elif ch1==3:
		hotelNum = input("请输入删除的宾馆编号(hotelNum):")
		sql = "delete from HOTELS where hotelNum = '%s'" % (hotelNum)
	# 删除客户
	else :
		custID = input("请输入删除的客户编号(custID):")
		sql = "delete from CUSTOMERS where custID = '%s'" % (custID)
	if exctDeleteSQL(sql):
		print("删除成功")
	else :
		print("删除失败")

# 查询(包含/不包含预定)
def Query(ch1):
	order = input("是否包含预定信息(Y/N)?")
	if order=="Y" or order=="y":
		# 查询航班预定信息
		if ch1==1:
			querySQL = "select %s \
						from RESERVATIONS natural join CUSTOMERS, FLIGHTS \
						where resvKey = flightNum and resvType = 1" % (FORMAT+", FromCity, ArivCity")
			flights = exctQuerySQL(querySQL)
			if len(flights)==0 :
				print("没有预定任何航班")
			else :
				# 显示航班信息
				print("所有预定航班信息如下:")
				print("custID, custName, resvNum, flightNum, price, FromCity, ArivCity")
				for each in flights :
					print(each)

		# 查询大巴车预定信息
		elif ch1==2:
			querySQL = "select %s \
						from RESERVATIONS natural join CUSTOMERS, BUS \
						where resvKey = busNum and resvType = 3" % (FORMAT+", location")
			buses = exctQuerySQL(querySQL)
			if len(buses)==0 :
				print("没有预定任何大巴车")
			else :
				# 显示大巴车信息
				print()
				print("所有预定大巴车信息如下:")
				print("custID, custName, resvNum, busNum, price, location")
				for each in buses :
					print(each)
			
		# 查询宾馆预定信息
		elif ch1==3:
			querySQL = "select %s \
						from RESERVATIONS natural join CUSTOMERS, HOTELS \
						where resvKey = hotelNum and resvType = 2" % (FORMAT+", location")
			hotels = exctQuerySQL(querySQL)
			if len(hotels)==0 :
				print("没有预定任何宾馆")
			else :
				# 显示宾馆信息
				print("所有预定宾馆信息如下:")
				print("custID, custName, resvNum, hotelNum, price, location")
				for each in hotels :
					print(each)
		# 查询客户预定信息
		else:
			querySQL = "select custID, custName, resvType, resvNum \
						from RESERVATIONS natural join CUSTOMERS order by custID"
			custs = exctQuerySQL(querySQL)
			if len(custs)==0 :
				print("没有客户预定")
			else :
				# 显示客户信息
				print("所有客户预定信息如下:")
				print("custID, custName, resvType, resvNum")
				for each in custs :
					print(each)

	else:
		# 查询航班
		if ch1==1:
			querySQL = "select * from FLIGHTS"
			flights = exctQuerySQL(querySQL)
			if len(flights)==0 :
				print("没有航班")
			else :
				# 显示航班信息
				print("所有航班信息如下:")
				print("flightNum, price, numSeats, numAvail, FromCity, ArivCity")
				for each in flights :
					print(each)

		# 查询大巴车
		elif ch1==2:
			querySQL = "select * from BUS"
			buses = exctQuerySQL(querySQL)
			if len(buses)==0 :
				print("没有大巴车")
			else :
				# 显示大巴车信息
				print("所有大巴车信息如下:")
				print("busNum, location, price, numSeats, numAvail")
				for each in buses :
					print(each)
			
		# 查询宾馆
		elif ch1==3:
			querySQL = "select * from HOTELS"
			hotels = exctQuerySQL(querySQL)
			if len(hotels)==0 :
				print("没有宾馆")
			else :
				# 显示宾馆信息
				print("所有宾馆信息如下:")
				print("hotelNum, location, price, numRooms, numAvail")
				for each in hotels :
					print(each)
		# 查询客户
		else:
			querySQL = "select * from CUSTOMERS"
			custs = exctQuerySQL(querySQL)
			if len(custs)==0 :
				print("没有客户")
			else :
				# 显示客户信息
				print("所有客户信息如下:")
				print("custID, custName")
				for each in custs :
					print(each)


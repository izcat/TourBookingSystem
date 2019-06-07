import pymysql

DataBaseUser = "root"
DataBasePassword = "1234" 
DataBaseName = "TourBooking"

FORMAT = "custName, custID, resvNum, resvKey, price"
FORMAT_FLIGHTS = "flightNum, price, numSeats, numAvail, FromCity, ArivCity"
FORMAT_BUS = "busNum, location, price, numSeats, numAvail"
FORMAT_HOTELS = "hotelNum, location, price, numRooms, numAvail"


# 执行MySQL添加
# 成功返回True, 失败返回False
def exctInsertSQL(sql):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	try:
		# 执行SQL语句
		cursor.execute(sql)
		db.commit()
		# 关闭数据库连接
		db.close()
		return True
	except:
		# 如果发生错误则回滚
		db.rollback()
		db.close()
	return False

# 执行MySQL删除
# 成功返回True, 失败返回False
def exctDeleteSQL(sql):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	try:
		# 执行SQL语句
		cursor.execute(sql)
		db.commit()
		# 关闭数据库连接
		db.close()
		return True
	except:
		# 如果发生错误则回滚
		db.rollback()
		db.close()
	return False

# 执行MySQL查询
# 返回全部所有表
def exctQuerySQL(sql):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()

	result = ()
	try:
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		result = cursor.fetchall()
	except:
		# 如果发生错误则回滚
		db.rollback()
	finally:
		# 关闭数据库连接
		db.close()
	return result

# exctUpdateSQL(sql):

def exctSQL(sql):
	# 打开数据库连接
	db = pymysql.connect("localhost", DataBaseUser, DataBasePassword, DataBaseName)
	# 使用cursor()方法获取操作游标
	cursor = db.cursor()
	try:
		# 执行SQL语句
		cursor.execute(sql)
		db.commit()
		# 关闭数据库连接
		db.close()
		return True
	except:
		# 如果发生错误则回滚
		db.rollback()
		db.close()
	return False


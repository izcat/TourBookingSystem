/*

HOTELS(String location, int price, int numRooms, int numAvail)；
BUS(String location, int price, int numBus, int numAvail)；
CUSTOMERS(String custName,custID)；
RESERVATIONS(String custName, int resvType, String resvKey) 

FLIGHTS (String flightNum, int price, int numSeats, int numAvail, String FromCity, String ArivCity)；（可以添加起飞时间和降落时间）
HOTELS(String hotelNum,String location, int price, int numRooms, int numAvail)；
BUS(String BusNum（bus编号）,String location, int price, int numBus(剩余座位数), int numAvail)；
CUSTOMERS(int custID,String custName)；
RESERVATIONS(String resvNum,String custID, int resvType, String resvKey)；

*/

# 创建数据库
create database TourBooking;
use TourBooking;

# 创建航班表
create table FLIGHTS(
	flightNum	varchar(5) not null,
	price		int check(price>0),
	numSeats	int check(numSeats>0),
	numAvail	int,
	FromCity	varchar(20),
	ArivCity	varchar(20),
	primary key(flightNum));

# 创建宾馆房间表
create table HOTELS(
	hotelNum	varchar(5) not null,
	location	varchar(50),
	price		int check(price>0),
	numRooms	int check(numRooms>0),
	numAvail	int,
	primary key(hotelNum));

# 创建大巴班车表
create table BUS(
	busNum		varchar(5) not null,
	location	varchar(50),
	price		int check(price>0),
	numSeats	int check(numsSeats>0),
	numAvail	int,
	primary key(busNum));

# 创建客户数据表
create table CUSTOMERS(
	custID		varchar(5) not null,
	custName	varchar(10) not null,
	primary key(custID));
	
# 创建预定表
create table RESERVATIONS(
	resvNum		varchar(5) not null,
	custID		varchar(5) not null,
	resvType	int check(resvType in (1, 2, 3)),
	resvKey		varchar(5) check(resvKey in 
						(select flightNum from FLIGHTS 
						 union select hotelNum from HOTELS 
						 union select busNum from BUS)),
	primary key(resvNum));
	
/*
create table RESERVATIONS(
	resvNum		varchar(5) not null,
	custID		varchar(5) not null,
	resvType	int check(resvType in (1, 2, 3)),
	resvKey		varchar(5) not null,
	foreign key(resvKey) references FLIGHTS(flightNum) or HOTELS(hotelNum) or BUS(busNum));
*/


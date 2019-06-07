# TourBookingSystem
数据库上机第3、4次实验内容


上机实验 3和4

##实验要求
基于MySQL，设计并实现一个简单的旅行预订系统。该系统涉及的信息有航班、大巴班车、宾馆房间和客户数据等信息。其关系模式如下：
FLIGHTS (String flightNum, int price, int numSeats, int numAvail, String FromCity, String ArivCity)；（可以添加起飞时间和降落时间）
HOTELS(String hotelNum,String location, int price, int numRooms, int numAvail)；
BUS(String BusNum（bus编号）,String location, int price, int numBus(剩余座位数), int numAvail)；
CUSTOMERS(int custID,String custName)；
RESERVATIONS(String resvNum,String custID, int resvType, String resvKey)；

## 实验假设
为简单起见，对所实现的应用系统作下列假设：
1.	在给定的一个班机上，所有的座位价格也一样；flightNum是表FLIGHTS的一个主码（primary key）。
2.	在同一个地方的所有的宾馆房间价格也一样；hotelNum是表HOTELS的一个主码。
3.	在同一个地方的所有大巴车价格一样；BusNum是表 BUS的一个主码。
4.	custID是表CUSTOMERS的一个主码。
5.	表RESERVATIONS包含着那些和客户预订的航班、大巴车或宾馆房间相应的条目，具体的说，resvType指出预订的类型（1为预订航班，2为预订宾馆房间，3为预订大巴车），而resvNum是表RESERVATIONS的一个主码，resvKey对应于预订的三种表的某个的主键。
6.	在表FLIGHTS中，numAvail表示指定航班上的还可以被预订的座位数。对于一个给定的航班（flightNum）,数据库一致性的条件之一是，表RESERVATIONS中所有预订该航班的条目数加上该航班的剩余座位数必须等于该航班上总的座位数。这个条件对于表BUS和表HOTELS同样适用。

##基本功能
应用系统应完成如下基本功能：
1．	航班，大巴车，宾馆房间和客户基础数据的入库，更新（表中的属性也可以根据你的需要添加）。
2．	预定航班，大巴车，宾馆房间。（取消预定功能）
3．	查询航班，大巴车，宾馆房间，客户和预订信息。（取消预定功能）
4．	查询某个客户的旅行线路。
5．	检查预定线路的完整性（线路是否合理：航班时间冲突）。
6．	其他任意你愿意加上的功能。

##上机报告
根据大作业的要求，建立数据库，插入一些数据，完成航班查询、预定、取消功能，注意体现数据库一致性的原则。
# 预定后
# 更新航班信息
create trigger flight_update after insert on RESERVATIONS
for each row
update	FLIGHTS
set		numAvail = numAvail - 1
where	new.resvType = 1 and flightNum = new.resvKey;

# 更新宾馆信息
create trigger hotel_update after insert on RESERVATIONS
for each row
update	HOTELS
set		numAvail = numAvail - 1
where	new.resvType = 2 and hotelNum = new.resvKey;

# 更新大巴信息
create trigger bus_update after insert on RESERVATIONS
for each row
update	BUS
set		numAvail = numAvail - 1
where	new.resvType = 3 and busNum = new.resvKey;


# 取消预定后
# 更新航班信息
create trigger flight_update2 after delete on RESERVATIONS
for each row
update	FLIGHTS
set		numAvail = numAvail + 1
where	old.resvType = 1 and flightNum = old.resvKey;

# 更新宾馆信息
create trigger hotel_update2 after delete on RESERVATIONS
for each row
update	HOTELS
set		numAvail = numAvail + 1
where	old.resvType = 2 and hotelNum = old.resvKey;

# 更新大巴信息
create trigger bus_update2 after delete on RESERVATIONS
for each row
update	BUS
set		numAvail = numAvail + 1
where	old.resvType = 3 and busNum = old.resvKey;
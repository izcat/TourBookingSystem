#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

const int tot = 20;
const char* CITY[5] = {"Wuhan", "Xi'an", "Beijing", "Shanghai", "Shenzhen"};
// const char* name[10] = {""}
int main()
{

/*	FILE *f = fopen("flight.sql", "w");
	srand(time(NULL));

	fprintf(f, "insert into FLIGHTS values");
	for(int i=1;i<=tot;i++)
	{
		for(int k=0;k<100000000;k++);
		int seats = 30+rand()%6*5;
		int from = rand()%5;
		int to = rand()%5;
		while(from==to) to = rand()%5;
		fprintf(f, "('1%04d', %d, %d, %d, \"%s\", \"%s\")%c\n", rand()%10000, 500+rand()%10*100-1, seats, seats, CITY[from], CITY[to], i==tot?';':',');
	}
	fclose(f);


	f = fopen("hotel.sql", "w");
	srand(time(NULL));
	
	fprintf(f, "insert into HOTELS values");
	for(int i=0;i<5;i++) {
		for(int k=0;k<100000000;k++);
		int num = rand()%5+2;
		int price = 200+rand()%6*50-2;
		int rooms = 50+rand()%10*5;
		for(int j=0;j<num;j++) {
			fprintf(f, "('2%04d', \"%s\", %d, %d, %d)%c\n", rand()%10000, CITY[i], price, rooms, rooms, (i==4&&j==num-1)?';':',');
		}
	}
	fclose(f);*/

	FILE *f = fopen("bus.sql", "w");
	srand(time(NULL));
	
	fprintf(f, "insert into BUS values");
	for(int i=0;i<5;i++) {
		for(int k=0;k<100000000;k++);
		int num = rand()%5+2;
		int price = 100+rand()%6*20;
		int seats = 40+rand()%6*5;
		for(int j=0;j<num;j++) {
			fprintf(f, "('3%04d', \"%s\", %d, %d, %d)%c\n", rand()%10000, CITY[i], price, seats, seats, (i==4&&j==num-1)?';':',');
		}
	}
	fclose(f);
	return 0;
}


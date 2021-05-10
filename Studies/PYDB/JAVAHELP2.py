import mysql.connector as mysql
import random

from password import passreturn

deptPlace = ["DELHI DEL", "NAGPUR NAG", "BOMBAY BOM", "HYDERABAD HYD", "GOA GOI", "PUNE PNQ", "NASHIK ISK"]

arrPlace = deptPlace[::-1]

Airline = ["Air India", "Indigo", "AirAsia India", "GoAir", "Vistara", "TruJet"]

SeatClass = ["E", "B"]

try:

    db = mysql.connect(host="localhost", user="root", passwd=passreturn(), database="test")

    print(db)

    cursor = db.cursor()

    select = """SELECT * FROM rawflight2;"""

    # flightNo = 20
    # airline = "Air India"
    # seatingClass = "E"
    # stops = 0

    # for i in range(1, 25):
    #     deptTime = random.randint(2, 20)
    #     columnNumber = 40000 + i - 1
    #     day = i
    #     daysFly = random.randint(1, 100)
    #     randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
    #     randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
    #     fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
    #     seatsAvailable = random.randint(2, 7)
    #     duration = "2h 0m"
    #     if randomDeptPlace != randomArrPlace:
    #         query = f"Insert into rawflight2 values({columnNumber},'{day}-5-21','{day}-5-21',{daysFly},'{randomDeptPlace}','{randomArrPlace}','{deptTime}:00','{deptTime+2}:00',{flightNo},'{airline}',{fare},{seatsAvailable},'{seatingClass}','{duration}',0,'','' )"
    #         cursor.execute(query)

    #     print(query)
    #     print(f"Inserted {i} times!")

    # cursor.execute(select)
    # print(cursor.fetchall())

    # 2021-04-13

    # q1 = """
    # CREATE TABLE RAWFLIGHT3(
    #     ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #     DEPT_DATE VARCHAR(100),
    #     ORIGIN VARCHAR(100),
    #     DESTINATION VARCHAR(100),
    #     DEPT_TIME VARCHAR(100),
    #     ARR_TIME VARCHAR(100),
    #     FLIGHT_NO INT,
    #     AIRLINE VARCHAR(100),
    #     TOTAL_FARE VARCHAR(5),
    #     SEATS_AVAIL INT,
    #     SEATING_CLASS VARCHAR(2),
    #     DURATION VARCHAR(100)
    # )
    # """

    # cursor.execute(q1)

    i = 0

    for year in range(2020, 2022):
        for month in range(1, 13):
            for day in range(1, 29):
                # print(f"{year}-{month}-{day}")
                duration = "2h 20m"

                if month < 10:
                    if day < 10:

                        for _ in range(20):

                            randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
                            randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
                            deptTimeNo = random.randint(1, 20)
                            deptTime = ""
                            arrTimeNo = deptTimeNo + 2
                            arrTime = ""
                            flightNo = random.randint(1, 99)
                            randomAirline = Airline[random.randint(0, len(Airline) - 1)]
                            fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
                            seats = random.randint(1, 9)
                            randomSeatClass = SeatClass[random.randint(0, len(SeatClass) - 1)]

                            if randomDeptPlace != randomArrPlace:
                                if deptTimeNo < 12:
                                    deptTime = f"{deptTimeNo}:20 AM"
                                else:
                                    deptTime = f"{deptTimeNo}:20 PM"

                                if arrTimeNo < 12:
                                    arrTime = f"{arrTimeNo}:40 AM"
                                else:
                                    arrTime = f"{arrTimeNo}:40 PM"

                                # print(f"Date is : {year}-0{month}-0{day}  Flight No. is {flightNo}")
                                query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-0{month}-0{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                cursor.execute(query)
                                # print(query)
                                # print(
                                #     f"values('{year}-0{month}-0{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                # )

                                i += 1

                            else:
                                print("Skipped")

                    else:

                        for _ in range(20):

                            randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
                            randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
                            deptTimeNo = random.randint(1, 20)
                            deptTime = ""
                            arrTimeNo = deptTimeNo + 2
                            arrTime = ""
                            flightNo = random.randint(1, 99)
                            randomAirline = Airline[random.randint(0, len(Airline) - 1)]
                            fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
                            seats = random.randint(1, 9)
                            randomSeatClass = SeatClass[random.randint(0, len(SeatClass) - 1)]

                            if randomDeptPlace != randomArrPlace:
                                if deptTimeNo < 12:
                                    deptTime = f"{deptTimeNo}:20 AM"
                                else:
                                    deptTime = f"{deptTimeNo}:20 PM"

                                if arrTimeNo < 12:
                                    arrTime = f"{arrTimeNo}:40 AM"
                                else:
                                    arrTime = f"{arrTimeNo}:40 PM"

                                # print(f"Date is : {year}-0{month}-0{day}  Flight No. is {flightNo}")
                                query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-0{month}-{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                cursor.execute(query)
                                # print(query)
                                # print(
                                #     f"values('{year}-0{month}-{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                                # )

                                i += 1

                            else:
                                print("Skipped")

                else:

                    for _ in range(20):

                        randomDeptPlace = deptPlace[random.randint(0, len(deptPlace) - 1)]
                        randomArrPlace = arrPlace[random.randint(0, len(arrPlace) - 1)]
                        deptTimeNo = random.randint(1, 20)
                        deptTime = ""
                        arrTimeNo = deptTimeNo + 2
                        arrTime = ""
                        flightNo = random.randint(1, 99)
                        randomAirline = Airline[random.randint(0, len(Airline) - 1)]
                        fare = f"{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
                        seats = random.randint(1, 9)
                        randomSeatClass = SeatClass[random.randint(0, len(SeatClass) - 1)]

                        if randomDeptPlace != randomArrPlace:
                            if deptTimeNo < 12:
                                deptTime = f"{deptTimeNo}:20 AM"
                            else:
                                deptTime = f"{deptTimeNo}:20 PM"

                            if arrTimeNo < 12:
                                arrTime = f"{arrTimeNo}:40 AM"
                            else:
                                arrTime = f"{arrTimeNo}:40 PM"

                            # print(f"Date is : {year}-0{month}-0{day}  Flight No. is {flightNo}")
                            query = f"Insert into rawflight3(DEPT_DATE,ORIGIN ,DESTINATION,DEPT_TIME,ARR_TIME ,FLIGHT_NO,AIRLINE ,TOTAL_FARE ,SEATS_AVAIL ,SEATING_CLASS,DURATION) values('{year}-{month}-{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                            cursor.execute(query)
                            # print(query)
                            # print(
                            #     f"values('{year}-{month}-{day}','{randomDeptPlace}','{randomArrPlace}','{deptTime}', '{arrTime}', {flightNo}, '{randomAirline}','{fare}', {seats}, '{randomSeatClass}', '{duration}')"
                            # )

                            i += 1

                        else:
                            print("Skipped")

    db.commit()
except Exception as e:
    print(e)
finally:
    db.close()

print(i)


# for year in range(2020, 2022):
#     for month in range(10, 13):
#         for day in range(10, 29):
#             # print(f"{year}-{month}-{day}")
#             # flightNo = random.randint(1, 99)
#             date = f"{year}-{month}-{day}"
#             print(date)

import matplotlib.pyplot as plt
import pandas
import mysql.connector
import datetime
import time
# connect to MySQL database 
db_connection = mysql.connector.connect(
host="localhost",
user="root",
passwd="root",
database="SensorData"
  )
db_cursor = db_connection.cursor()
    
#    queryTR = """ 
#   SELECT Date, Temp 
#   FROM SensorR  
#   WHERE Date >= "2020-02-23  8:00:40"
#      AND Date < "2020-02-28  16:20:00"; 
#    """
#    dTR = pandas.read_sql(queryTR, db_connection, index_col=['Date'])
Sensor = raw_input("Sensor name SensorP or SensorR?  ")
A = raw_input("how many days in the past?  ")
  

# this is the query we will be making 
queryT = """ 
SELECT Date, Temp 
FROM %s 
WHERE Date BETWEEN NOW() - INTERVAL '%s' DAY AND NOW(); 
""" % (Sensor,A) 
dT = pandas.read_sql(queryT, db_connection, index_col=['Date'])

queryP = """ 
SELECT Date, Pressure 
FROM %s   
WHERE Date BETWEEN NOW() - INTERVAL '%s' DAY AND NOW(); 
""" % (Sensor,A)  
dP = pandas.read_sql(queryP, db_connection, index_col=['Date'])

queryH = """ 
SELECT Date, Humidity
FROM %s  
WHERE Date BETWEEN NOW() - INTERVAL '%s' DAY AND NOW(); 
""" % (Sensor,A)  
dH = pandas.read_sql(queryH, db_connection, index_col=['Date'])

with open('PPPDATA2-10-2020.txt', 'r') as s:
            lines = s.readlines()
            datesp = [str(line.split()[0]) for line in lines]
            
            yp = [float(line.split(",")[1]) for line in lines]
            zp = [float(line.split(",")[2]) for line in lines]
            wp = [float(line.split(",")[3]) for line in lines]
            datep = [datetime.datetime.strptime(x,'%m/%d/%Y-%H:%M:%S') for x in datesp]

plt.subplot(3,1,1)
plt.title('Temperature, Humidity, and Pressure')
plt.ylabel('Temperature' + u'\u2103')
plt.plot(dT, color='red')

#plt.plot(datep, yp, 'r.-', color='blue')
plt.grid(True)
            

plt.subplot(3,1,2)
plt.plot(dP, color='red')

#plt.plot(datep, wp, 'r.-', color='blue')
plt.xlabel('Time')
plt.ylabel('Presure KPA'.decode('unicode-escape'))
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(dH, color='red')

#plt.plot(datep, zp, 'r.-', color='blue')
plt.xlabel('Time')
plt.ylabel('Humidity RH%'.decode('unicode-escape'))
plt.grid(True)

plt.savefig('/home/pi/flask/static/images/CompareGraph.png')
print(datetime.datetime.strptime(x,'%m/%d/%Y-%H:%M:%S'))
plt.show()
db_connection.close()


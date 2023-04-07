import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='TRS'
)

mycursor = mydb.cursor(buffered=True)


tno=[1,2,3,4,5,6,7,8,9,10,11,12]
tnames=["Double Decker","Brindavan Express","Shadapti Express","Sangamitra SF express","Bengaluru Mail","Passenger Memu 1","Guruvayur Express","Ananthapuri Express","Thiruvananthapuram Central Mail","Passenger Memu 2",'Taliban Express','Fidel Castro Express']
troutes=["ctobe","ctobe","ctobe","ctobe","ctobp","ctobp","ctote","ctote","ctote","ctotp"]
times=[4,5,6,7,8,9,4,5,6,7,8,9]
a=0
while a<10:
    sql=f"insert into train values({tno[a]},'{tnames[a]}','{troutes[a]}','{times[a]}')"
    mycursor.execute(sql)
    mydb.commit()
    a+=1


"""
sql="select*from train ORDER BY tno asc"
mycursor.execute(sql)
a=mycursor.fetchall()
print(a)
"""
"""
stops=["MGR Chennai Central","Perambur","Arakkonam Junction","Sholaingnallur","Walajah Road Junction","Katpadi Junction","Gudiyatham","Ambur","Vaniyambadi","Jolarpettai Junction","Patchur","Malanur","Kuppam","Gudupalli","Kamasamudram","Bangarpet Junction","Tyakal","Malur","Devangonthi","White Field","Krishnarajapuram","Bengaluru East","Bengaluru Cantt.","KSR Bengaluru City junction"]
eorp=['e', 'p', 'e', 'p', 'p', 'e', 'p', 'e', 'e', 'e', 'p', 'p', 'e', 'p', 'p', 'e', 'p', 'p', 'p', 'p', 'e', 'p', 'e', 'e']
a=0
for i in range(len(stops)):
    sql=f"insert into ctob values('{stops[a]}','{eorp[a]}')"
    mycursor.execute(sql)
    mydb.commit()
    a+=1
"""


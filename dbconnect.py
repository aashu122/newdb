# CRUD
import pymysql
connection = pymysql.connect(host = "localhost",db = "test", user = "root", password = "root")
cur = connection.cursor()
def create():
    try:
        name = input("Enter the name: ")
        standard = input("Enter the class: ")
        city =  input("Enter the city: ")
        state = input("Enter the state: ")
        avg = float(input("Enter the avg marks: "))
        cur.execute("insert into student(name, standard, city, state, avg) values('{}','{}','{}','{}','{}')".format(name,standard,city,state,avg))
        connection.commit()
    except:
        print("Invalid input")
def display():
    cur.execute("select * from student")
    data = cur.fetchall()
    print("sid Name     standard       city         state        Avg")
    for i in data:
        print("% -4d% - 10s% - 13s% - 15s% -10s% - .1f"%(i[0],i[1],i[2],i[3],i[4],i[5]))
def search():
    try:
        num = int(input("Enter the SID to search: "))
        cur.execute("select * from student where sid = %d" %num)
        data = cur.fetchone()
        # If want to use fetchall then you have to use for loop because fetch all return mutiple rows of data
        if (data == None):
            print("No such Type Record Available ")
        else:
            print("Sid Name Standard city state Avg ")
            print("% -4d% - 15s% - 11s% - 8s% - 6s% -.1f"%(data[0],data[1],data[2],data[3],data[4], data[5]))
    except:
        print("Invalid Input")
def edit():
    try:
        num = int(input("Enter the sid to edit: "))
        avg = float(input("Enter Avg Marks to Update: "))
        cur.execute("Update student set avg = %f where sid = %d"%(avg,num))
        connection.commit()
    except:
        print("Invaid Input")
def delete():
    try:
        num = int(input("Enter the SID to Delete: "))
        cur.execute("Delete from student where sid = %d"%num)
        connection.commit()
    except:
        print("Invalid Input")
while(True):
    choice = int(input("\n\n\nCRUD\nmenu\n1. Create a Record\n2.Display\n3. Search\n4. Edit\n5. Delete\n6. exit\n"))
    if choice == 1:
        create()
    elif choice == 2:
        display()
    elif choice == 3:
        search()
    elif choice == 4:
        edit()
    elif choice == 5:
        delete()
    elif choice == 6:
        connection.close()
        break
    else:
        print("Invalid Choice")

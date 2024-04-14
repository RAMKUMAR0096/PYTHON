import mysql.connector
con=mysql.connector.connect(host="localhost",username="root",password="",database="student_list")


def add(name,gen,age,address):
    res=con.cursor()
    sql="insert into students(name,gender,age,address) values(%s,%s,%s,%s)"
    det=(name,gen,age,address)
    res.execute(sql,det)
    con.commit()
    print(name,"register sucessfully")

def update(name,gen,age,address,id):
    res=con.cursor()
    sql="update students set name=%s,gender=%s,age=%s,address=%s where id=%s"
    det=(name,gen,age,address,id)
    res.execute(sql,det)
    con.commit()
    print(name,"Update sucessfully")

def delete(id):
    res=con.cursor()
    sql="delete from students  where id=%s"
    det=(id,)
    res.execute(sql,det)
    con.commit()
    print("deleted sucessfully")

def show():
    res=con.cursor()
    sql="select * from students"
    res.execute(sql)
    result=res.fetchall()
    print(result)

while (True):
    print("1.Add student detail")
    print("2.Update student detail")
    print("3.Delete student detail")
    print("4.Show student detail")
    print("5.exit")
    choice=int(input("Enter your choice:"))
    if (choice==1):
        name=input("Enter your name:")
        gen=input("Enter the gender:")
        age=input("Enter yoour age:")
        address=input("Enter your address:")
        add(name,gen,age,address)
    elif choice==2:
        id=int(input("Enter the id update:"))
        name=input("Enter your name:")
        gen=input("Enter the gender:")
        age=input("Enter yoour age:")
        address=input("Enter your address:")
        update(name,gen,age,address,id)
    elif choice==3:
        id=input("Enter the id to delete:")
        delete(id)
    elif choice==4:
        show()
    elif choice==5:
        quit()
    else:
          print("Invalid selection ** Please tryagain......")
 

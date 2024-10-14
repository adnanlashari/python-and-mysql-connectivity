import mysql.connector as sql
import bcrypt

db=sql.connect(
    user="adnan",
    password="Adnan@123",
    host="",
    database="acountt_management"
)
mysql_data=db.cursor()

"""def insert_owner(id,name,password):
   # hashpass=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    data=(f"insert into owner(id,name,password)values(%s,%s,%s)")
    mysql_data.execute(data,(id,name,password))
    db.commit()
    print("owner data adding seccessfully")"""

# owner_id=int(input("enter owner id : "))
# owner_name=input("enter owner name : ")
# owner_password=input("enter ther admin password : ")

"""insert_owner(8765,"Tauqeer","tauqeer")"""

# def insert_admin(id,name,password):
#     #hashpass=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
#     data=(f"insert ignore into admin(id,name,password)values(%s,%s,%s)")
#     mysql_data.execute(data,(id,name,password))
#     db.commit()
#     print("admin data is inserting")
# admin_id=int(input("enter admin id : "))
# admin_name=input("enter admin name : ")
# admin_password=input("enter admin password : ")
# insert_admin(admin_id,admin_name,admin_password)

# mysql_data.execute("")
def add_expenses():

    id = int(input("Enter your id who is adding expenses: "))
    amount=int(input("enter the amount of expenses : "))
    created_date=input("enter the date with month and year : ")
    purpose=input("enter the purpose of expenses : ")
    

    admin_approvel = input("Do you want to approve this expense (yes/no): ")
    if admin_approvel == 'yes'.lower():
        data=(f"insert ignore into expenses(amount,created_date,purpose,id)values(%s,%s,%s,%s)")
        val = (amount,created_date,purpose,id)
        mysql_data.execute(data,val)
        db.commit()
        print("expenses are inserting")

    else:
        print('Rejected')




def add_income():

     enter_income=(f"insert ignore into income(amount,created_date,id)values(%s,%s,%s)")
     val=(amount,created_date,id)
     mysql_data.execute(enter_income,val)
     db.commit()
     print("income is added to your account")

     


def monthly_report():
    mysql_data.execute("select * from income where created_date like '%04%'")
    report_monthly=mysql_data.fetchall()
    for i in report_monthly:
       print(i)
    

  
def yearly_report():
    mysql_data.execute("select * from income where created_date like '2024%'")
    report_yearly=mysql_data.fetchall()
    for i in report_yearly:
       print(i)
    


def weekly_report():
    mysql_data.execute("select * from income where created_date between '2024-10-11' AND '2024-10-17'")
    report_weekly=mysql_data.fetchall()
    for i in report_weekly:
        print(i)

      
runing=True
while runing==True:
    print("...enter your choice...\n 1:....add_expenses\n 2:....add_income \n 3:....weekly_report \n 4:....monthly_report\n 5:....yearly_report \n 0:.... exit")
    choice=int(input("enter your choice"))
    if choice==1:
        add_expenses()
        
    elif choice ==2:
        amount=int(input("enter the amount of income : "))
        created_date=input("enter the date first yeas then month and last day : ")
        id=input("enter the id from which income is coming : ")

        add_income()
    elif choice==3:
        weekly_report()
    elif choice==4:
        monthly_report()
    elif choice==5:
        yearly_report()
    elif choice==0:
        runing=False
        print("exit")
    else:
        runing=False
        print("exit")
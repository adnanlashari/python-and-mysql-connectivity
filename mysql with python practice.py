import mysql.connector

class Website:
  def __init__(self):
    self.db=mysql.connector.connect(
      user="adnan",
      password="Adnan@123",
      host="",
      database="account_management"
    )
    self.cursor=self.db.cursor()

  def commit(self):
    self.db.commit()

  def update_employee(self):
    sql="update employee set salary=50001 where id=4456"
    self.cursor.execute(sql)
    self.commit()

  def update_expense(self):
    sql="update expense set weekly_exp=40000 where name='Enigmatix'"
    self.cursor.execute(sql)
    self.commit()

  def add_employee(self,id,name,salary,email,contact,company_id):
    sql=("insert into employee(id,name,salary,email,contact,company_id) values (%s,%s,%s,%s,%s,%s)")
    values = (id,name,salary,email,contact,company_id)
    self.cursor.execute(sql,values)
    self.commit()
    print("employee added")

  def show_employee(self):
    print("Here is the list of employee: ")
    self.cursor.execute("select * from employee")
    record = self.cursor.fetchall()
   
    for i in record:
      print(i)
    
cnx = Website()
#cnx.add_employee(4459,"Muhammad Kabeer",40000,"kabeer@gmail.com",2058301,2144)
# update_employee()
# update_expense()
  
cnx.show_employee()
  
  




import mysql.connector as sql

class my_data:
    def __init__(self):
        self.cnx = sql.connect(
            host='localhost',
            user='root',
            password='123',
            database='Enigmatix'
        )

        self.cursor = self.cnx.cursor()

    def add_user(self, users_id, users_name, users_password):

        data = ("insert into Enigmatix_users(users_id,users_name,users_password) values (%s,%s,%s)")
        self.cursor.execute(data, (users_id, users_name, users_password))
        self.cnx.commit()
        print("~~~ user is added ~~~ ")

    def delete_user(self, users_id):
        delete = (f"delete from Enigmatix_users where users_id={users_id}")
        self.cursor.execute(delete)
        self.cnx.commit()
        print(" ~~~ user is deleted ~~~ ")


    def update_user_password(self, users_id, users_password):
        update = ("update Enigmatix_users set users_password=%s where users_id=%s")
        self.cursor.execute(update,(users_password, users_id))
        self.cnx.commit()
        print(" ~~~ password is updated ~~~ ")


    def display_user_data(self):
        display = ("select * from Enigmatix_users")
        self.cursor.execute(display)
        data = self.cursor.fetchall()
        for i in data:
         print(i)

    def owner_login(self, owner_name, owner_password):
        data = ("select * from Enigmatix_owner where owner_name=%s and owner_password=%s")
        self.cursor.execute(data, (owner_name, owner_password))
        fetch = self.cursor.fetchone()
        if fetch:
            print(" ~~~ login successfully ~~~ ")
            return True
        else:
            print(" ~~~ owner_name or password wrong ~~~ ")
            return False

    def admin_login(self, admin_name, admin_password):
        data = ("select * from Enigmatix_admin where admin_name=%s and admin_password=%s")
        self.cursor.execute(data, (admin_name, admin_password))
        fetch = self.cursor.fetchone()
        if fetch:
            print(" ~~~ login successfully ~~~ ")
            return True
        else:
            print(" ~~~ name or password wrong ~~~ ")
            return False

    def user_login(self, users_id, users_name, users_password):
        data = ("select * from Enigmatix_users where users_id=%s and users_name=%s and users_password=%s")
        self.cursor.execute(data, (users_id, users_name, users_password))
        fetch = self.cursor.fetchone()
        if fetch:
            print(" ~~~ login successfully ~~~ ")
            return True
        else:
            print(" ~~~ you entered wrong please enter correct and Try again ~~~ ")
            return False

    def add_expenses(self, users_id, expenses_amount):
        admin_approvel = input("enter admin_password: ")
        if admin_approvel == 'saad@123':
            print(" ~~~ accepted ~~~ ")


            data = ("insert into Enigmatix.expenses(users_id,expenses_amount) values (%s,%s)")
            self.cursor.execute(data, (users_id, expenses_amount))

            self.cnx.commit()
            print(" ~~~ expense amount is added ~~~ ")
            return True

        else:
            print(" ~~~ rejected ~~~ ")
            return False
    def add_income(self, users_id,created_date, income_amount):

        data = (f"insert into Enigmatix.income(users_id,created_date,income.income_amount) values (%s,%s,%s)")
        self.cursor.execute(data, (users_id,created_date, income_amount))
        self.cnx.commit()
        print(" ~~~ income amount is added ~~~ ")

    def show_expenses(self):
        show = ("select expenses_amount from Enigmatix.expenses")
        self.cursor.execute(show)
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def show_income(self):
        show = ("select income_amount from Enigmatix.income")
        self.cursor.execute(show)
        data = self.cursor.fetchall()
        for i in data:
            print(i)


    def fun_call(self,choice):
        print("...enter your choice...\n 1:....add_users : \n 2:....delete_users: \n 3:....update_user_password : \n 4:....display_user_data : \n"
        " 5:....owner_login : \n6:....admin_login: \n7:....user_login : \n8:....add_expenses : \n9:....add_income : \n10:....show_expense : \n11:....show_income : ")
        choice = int(input("enter your choice : "))
        if choice == 1:
                id=int(input("enter the id of user : "))
                username=input("enter the user name : ")
                userpassword=input("enter the password of user : ")
                my_obj.add_user(id,username,userpassword)

        elif choice == 2:
                id = int(input("enter the id of user : "))
                my_obj.delete_user(id)

        elif choice == 3:
                 id = int(input("enter the id of user : "))
                 userpassword = input("enter the password of user : ")
                 my_obj.update_user_password(id,userpassword)
        elif choice == 4:
                  my_obj.display_user_data()
        elif choice == 5:
                  owner_name=input("enter company owner name : ")
                  owner_password=input("enter owner password : ")
                  my_obj.owner_login(owner_name,owner_password)
        elif choice == 6:
                   admin_name=input("enter company admin name : ")
                   admin_password=input("enter admin password : ")
                   my_obj.admin_login(admin_name,admin_password)
        elif choice==7:
                   user_id=input("enter user id : ")
                   user_name=input("enter company user name : ")
                   user_password=input("enter user password : ")
                   my_obj.user_login(user_id,user_name,user_password)
        elif choice==8:
                   id = int(input("enter id of user : "))
                   expenses_amount = int(input("enter the amount of expense : "))
                   my_obj.add_expenses(id, expenses_amount)
        elif choice==9:
                   id = int(input("enter id of user : "))
                   date=input("enter the date year/month/week : ")
                   income_amount = int(input("enter the amount of expense : "))
                   my_obj.add_income(id, date,income_amount)
        elif choice==10:
                  my_obj.show_expenses()
        elif choice==11:
                  my_obj.show_income()

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            my_obj.fun_call("1")
        else:
            print("exit")

my_obj = my_data()
my_obj.fun_call("1")










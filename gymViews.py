from mysql import connector
from datetime import datetime

class DbConnect:
    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Jis12#na",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            q = "select * from member"
            self.cursor.execute(q)
            records = self.cursor.fetchall()
            # for data in records:
            #     print(data)
            return records
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            q = "insert into member(name, place, mobile, plan, fee, joined_date) values (%s, %s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(q, values)
            self.connect.commit()
            # print("Member Added Successfully!")
        except Exception as e:
            print(e)

    def get_obj(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            q = 'select * from member where id = %s'
            v = (id,)
            self.cursor.execute(q, v)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def retrieve(self, id=None):
        try:
            record = self.get_obj(id)
            if record != None:
                print("- - - MEMBER DETAILS - - -")
                print(record)
            else:
                print("Member Not Found!")
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_obj(id)
            if record != None:
                self.connect = super().get_connected()
                self.cursor = self.connect.cursor()
                q = 'delete from member where id = %s'
                v = (id,)
                self.cursor.execute(q, v)
                self.connect.commit()
                print("Member Deleted!")
            else:
                print("Member Not Found")
        except Exception as e:
            print(e)

    def put(self, id= None, **kwargs):
        try:
            record = self.get_obj(id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ''
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                q = f"update member set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(q, values)
                self.connection.commit()
                print("Member Details Updated!")
                self.retrieve(id)
            else:
                print("Member Not Found!")
        except Exception as e:
            print(e)


# connect_instance = DbConnect()
# print(connect_instance.get_connected())

# member_instance = GymMemberManager()
# member_instance.post(name= "Manu", place= "Tvm", mobile= 8796541230, plan= "1 month", fee= 1000, joined_date= datetime.today())
# member_instance.post(name= "Hari", place= "Kochi", mobile= 7596840123, plan= "3 month", fee= 2800, joined_date= datetime.today())
# member_instance.post(name= "Anu", place= "Calicut", mobile= 8659320147, plan= "6 month", fee= 5600, joined_date= datetime.today())
# member_instance.post(name= "Ashley", place= "Kannur", mobile= 9685320174, plan= "3 month", fee= 2800, joined_date= datetime.today())
# member_instance.get()
# member_instance.retrieve(3)
# member_instance.delete(4)
# member_instance.put(1, name= 'Arya', place= 'Kottayam')

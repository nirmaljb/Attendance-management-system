import mysql.connector
import creds

class Auth:
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=creds.password,
            database="login_info"
        )
        cursor = mydb.cursor()
        cursor.execute('Select * from credentials')
        self.results = cursor.fetchall()
    
    def auth(self, username, password):
        for _name, _pass in self.results:
            if username == _name:
                if password == _pass:
                    return [True, _name, _pass]
        return [False, username, password]
    
class Student:
    def __init__(self, class_no, section_id):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=creds.password,
            database="students"
        )
        self.class_no = class_no
        self.section = section_id

    def attend(self, student, student_roll):
        no_of_days_present = student[4] + 1
        calc = (no_of_days_present / 2.2)

        query = f"UPDATE class_{self.class_no}_{self.section_id} SET Present_days={no_of_days_present}, Present_percent={calc} WHERE Roll_no={student_roll}"

        self.cursor.execute(query)
        self.mydb.commit()

    def add(self, student_roll, first_name, last_name, present_days):
        calc = (present_days / 2.2)
        query = f'INSERT into class_{self.class_no}_{self.section} (Roll_no, First_name, Last_name, Present_days, Total_days, Present_Percent) VALUES ({student_roll},{first_name},{last_name},{present_days},{calc})'

        self.cursor.execute(query)
        self.mydb.commit()
    
    def remove(self, student_roll):
        query = f''

        self.cursor.execute(query)
        self.mydb.commit()

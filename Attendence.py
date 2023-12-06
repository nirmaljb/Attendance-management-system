from Connector import Student

class Attendence:
    def __init__(self, class_no=12, section='d'):
        self.class_no = class_no
        self.section = section
        self.system = Student(class_no, section)
        
        self.process()
    
    def process(self):        
        students = Student.get_all_students()

        for student in students:
            student_name = f'{student[2]} {student[3]}'
            student_roll = student[1]

            vote = input(f'is {student_name} present today?(y/n) : ')

            if vote.lower() == 'y':
                self.system.attend(student, student_roll)
            elif vote.lower() == 'n':
                continue
  

    def show(self, class_no=12, section='d'):

        cursor = self.mydb.cursor()
        cursor.execute(f"Select * from class_{class_no}_{section}")
        result = cursor.fetchall()

        for student in result:
            print(student)


from Connector import Student

class Admin:
    def __init__(self, class_no, section_id):
        self.class_no = class_no
        self.section_id = section_id
        self.agent = Student(self.class_no, self.section_id)
    
    def add_new_student(self, roll_no, first_name, last_name, present_days): 
        #add a condition *
        
        self.agent.add(roll_no, first_name, last_name, present_days)

        print(f'{first_name} {last_name} has been successfully added to class {self.class_no} section {self.section_id}')
    
    def remove_student(self, roll_no):
        # add a condition *
        self.agent.remove(roll_no)

        #write a print statement
        print(f'Student with Roll no = {roll_no} has been successfully removed to class {self.class_no} section {self.section_id}')
    
    def get_particular_student_info(self, roll_no):
        # add a condition *
        student = self.agent.student_info(roll_no)

        for stud in student:
            roll_no = stud[1]
            fullname = f'{stud[2]} {stud[3]}'
            present_day = stud[4]
            present_percent = stud[5]

        print(f'Roll no = {roll_no}, Fullname = {fullname} No of days present = {present_day} Percentage of days present = {present_percent}%')

    def get_all_students(self):
        students = self.agent.get_all_students()

        for stud in students:
            roll_no = stud[1]
            fullname = f'{stud[2]} {stud[3]}'
            present_day = stud[4]
            present_percent = stud[5]

            print(f'Roll no = {roll_no}, Fullname = {fullname} No of days present = {present_day} Percentage of days present = {present_percent}%')



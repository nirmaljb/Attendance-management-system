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
        
        # add a condition
        self.agent.remove(roll_no)

        #write a print statement
        print('')

    

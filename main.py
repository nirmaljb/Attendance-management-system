from Connector import Auth
import Attendence, Admin

def admin():
    class_ = input('What is your class ? (eg. 12) : ').lower()
    section_ = input('What is your section? (a/b/c/d) : ').lower()

    Agent = Admin(class_, section_)

    print('Press 1 to add a new student.')
    print('Press 2 to remove a student.')
    print('Press 3 to get the info of a specific student.')
    print('Press 4 to get the info of all students.')

    # add a condition * 
    choice = int(input('Enter your choice : '))

    match choice:
        case 1:
            # ability to add students in according to class and section
            # roll_no, first_name, last_name, present_days
            roll_no = int(input('Enter roll number : '))
            first_name = input('Enter first name : ')
            last_name = input('Enter last name : ')
            present_days = int(input('Enter the number of days, the student is present : '))

            Agent.add_new_student(roll_no, first_name, last_name, present_days)
        case 2:
            # ability to remove student in according to class and section
            roll_no = int(input('Enter roll number : '))
            Agent.remove_student(roll_no)
        
        case 3:
            # ability to see the info of a specific student (days present, percentage of days present)
            roll_no = int(input('Enter roll number : '))
            Agent.get_particular_student_info(roll_no)
        case 4:
            # ability to see the info of all students (days present, percentage of days present)
            Agent.get_all_students()

def teacher():
    class_ = input('What is your class ? (eg. 12) : ').lower()
    section_ = input('What is your section? (a/b/c/d) : ').lower()

    Attendence.Attendence(class_, section_)

    print('Students list ended, system ended.')


status = False
Agent = Auth()

while status != True:
    username = input('Please enter your username : ').lower()
    password = input('Please enter your password : ').lower()
    choice = input('Are you an admin or teacher ? (a/t) : ').lower()
    status = Agent.auth(username, password)[0]

if choice == 'a':
    admin()
elif choice == 't':
    teacher()

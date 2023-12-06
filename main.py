from Connector import Auth
import Attendence

Agent = Auth()


def admin():
    # ability to add students in according to class and section
    
    # ability to remove student in according to class and section

    # ability to see the info of a specific student (days present, percentage of days present)

    # ability to see the info of all students (days present, percentage of days present)
    pass

def teacher():
    class_ = input('What is your class ? (eg. 12) : ').lower()
    section_ = input('What is your section? (a/b/c/d) : ').lower()

    Attendence.Attendence(class_, section_)

    print('Students list ended, system ended.')


status = False

while status != True:
    username = input('Please enter your username : ').lower()
    password = input('Please enter your password : ').lower()
    choice = input('Are you an admin or teacher ? (a/t) : ').lower()
    status = Agent.auth(username, password)[0]

if choice == 'a':
    admin()
elif choice == 't':
    teacher()

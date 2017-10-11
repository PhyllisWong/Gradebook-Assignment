import random
import datetime
import time
import uuid
from Students import Students

class Classroom():
    # This is going to be the class function
    possible_courses = ['Mathematics', 'Science', 'English', 'Economics', 'Social Studies', 'Geology']
    random_course = random.choice(possible_courses)
    chosen_course = random_course
    list_of_assignments = []
    class_roster = []

    def __init__(self):
        self.roster = []
    def courses(self):
        # This essentially tells the students what the courses will be
        print('Hello new student this is %s' %(random_course))

    def times_courses_meet(self):
        # This is essentially the function that will determine when the courses meet
        course_times = 'This course meets %s every Monday, Tuesday, and Friday' %(time.strftime('%H:%M:%S'))
        return(course_times)

    def create_course_id(self):
        # This is essentially the function that will give the course a course id
        for course in possible_courses:
            unique_identification = uuid.uuid4(course)

    def course_roster(self):
        # This will essentially be the roster for the class and the students that populate the class
        action = str(input)
        if action == 'create':
            print('What is the name of the student that you would like to add to the roster?')
            student

    def assignments(self):
        # Handles the assignment functionality such as assigning updating and deleting
        print("What do you want to do to assignments?")
        action = str(input)
        if action == 'create':
            # This essentially creates the assignment
            print('What is the name of the assignment?')
            assignment_name = input()
            course_assignemnts = self.list_of_assignments.append(assignment_name)
            return(course_assignemnts)
        if action == 'delete':
            # This essentially deletes an assignment
            assignment_name = input()
            if assignment_name not in self.list_of_assignments:
                print('The assignment you are trying to delete does not exist')
                return
            else:
                del self.list_of_assignments[assignment_name]
        if action == 'edit':
            # This essentially edits or updates an assignment
            print('Which assignment are you trying to edit?')
            original_assignment = input()
            edited_assignment = input()
            if original_assignment not in self.list_of_assignments:
                print('Sorry you can not edit an assignment that does not exist!')
                return
            else:
                new_assignment_name = self.list_of_assignments[original_assignment] = edited_assignment
                return(new_assignment_name)

    def create_student(self, student_name):
        # Now that the students are essentially being added to the roster
        new_student = Students(student)
        self.roster.append(new_student)
        return(roster)

    def class_roster(self):
        roster_dictionary = {}
        for student in self.roster:
            roster_dictionary[random_course] = student
            # This essentially creates the roster dictionary


# if __name__ == '__main__':
#     # Turn this on in debug mode to get detailled information about request related exceptions: http://flask.pocoo.org/docs/0.10/config/

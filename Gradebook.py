import random
import datetime
import time
import uuid

class Classroom():
    # This is going to be the class function
    possible_courses = ['Mathematics', 'Science', 'English', 'Economics', 'Social Studies', 'Geology']
    random_course = random.choice(possible_courses)
    list_of_assignments = []

    def courses(self):
        # This assigns the courses to the
        print('Hello new student this is %s' %(random_course))

    def times_courses_meet(self):
        # This is essentially the function that will determine when the courses meet
        print('This course meets %s every Monday, Tuesday, and Friday' %(time.strftime('%H:%M:%S')))

    def create_course_id(self):
        # This is essentially the function that will give the course a course id
        for course in possible_courses:
            unique_identification = uuid.uuid4(course)

    def course_roster(self):

        # This is essentially the roster for the course that is chosen
        # The keys will be the random course while the values
        # are the students that populate the course

        # roster_dictionary = {random_course: }
        pass

    def assignments(self):
        # Handles the assignment functionality such as assigning updating and deleting
        action = str(input)
        if action == 'create':
            print('What is the name of the assignment?')
            assignment_name = input()
            self.list_of_assignments.append(assignment_name)
        if action == 'delete':
            assignment_name = input()
            if assignment_name not in self.list_of_assignments:
                print('The assignment you are trying to delete does not exist')
                return
            else:
                del self.list_of_assignments[assignment_name]
        if action == 'edit':
            print('Which assignment are you trying to edit?')
            original_assignment = input()
            edited_assignment = input()
            if original_assignment not in self.list_of_assignments:
                print('Sorry you can not edit an assignment that does not exist!')
                return
            else:
                self.list_of_assignments[original_assignment] = edited_assignment

import random
import datetime
import time
import uuid

class Class():
    # This is going to be the class function
    possible_courses = ['Mathematics', 'Science', 'English', 'Economics', 'Social Studies', 'Geology']
    random_course = random.choice(self.possible_courses)
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
        roster_dictionary = {random_course: }

import random
import datetime
import time

class Class():
    # This is going to be the class function
    possible_courses = ['Mathematics', 'Science', 'English', 'Economics', 'Social Studies', 'Geology']
    def courses(self):
        # This assigns the courses to the
        print('Hello new student this is %s' %(random.choice(self.possible_courses)))

    def times_courses_meet(self):
        # This is essentially the function that will determine when the courses meet
        print('This course meets %s every Monday, Tuesday, and Friday' %(time.strftime('%H:%M:%S')))

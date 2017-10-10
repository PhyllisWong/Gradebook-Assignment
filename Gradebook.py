import random

class Class():
    # This is going to be the class function
    def courses(self):
        # This assigns the courses to the
        possible_courses = ['Mathematics', 'Science', 'English', 'Economics', 'Social Studies', 'Geology']
        print('Hello new student this is %s' %(random.choice(possible_courses)))

    

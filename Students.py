class Students():
    def __init__(self, name):
        # SEvery instance of this class will have a name of the student
        # and from there we will append it to an array
        self.name = name
        # Every student has an array of courses
        self.courses = []

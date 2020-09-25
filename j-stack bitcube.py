class STUDENT:

    def __init__(self, forenames, surname, email, date_of_birth, degree):
        self.forenames = forenames
        self.surname = surname
        self.email = email
        self.date_of_birth = date_of_birth
        self.degree = degree
        #self.firstname = forenames
        #self.fullname = forenames + surname

    def firstname(self):
        print(self.forenames[0])

    def fullname(self):
        print(f'{self.forenames} {self.surname}')


class LECTURER:

    def __init__(self, forenames, surname, email, date_of_birth):
        self.forenames = forenames
        self.surname = surname
        self.email = email
        self.date_of_birth = date_of_birth
        self.degrees = [degrees]
        #self.firstname = forenames
        # self.fullname = forenames surname

    def firstname(self):
        print(self.forenames[0])

    def fullname(self):
        print(f'{self.forenames} {self.surname}')


class DEGREE:

    def __init__(self, degree_name, duration, courses, lecturer):
        self.degree_name = degree_name
        self.duration = duration
        self.courses = courses
        self.lecturer = lecturer


class COURSE:

    def __init__(self, course_name, duration, courses, degree):
        self.course_name = course_name
        self.duration = duration
        self.courses = courses
        self.degree = degree


std1 = STUDENT(['Craig', 'Fred'], 'David',
               'craig.david@campus.com', '20/02/91', 'Geology')
print(std1.degree)

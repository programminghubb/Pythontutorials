# defining parent class College
class College:

    def __init__(self, name, mob_num):
        self.name = name
        self.mob_num = mob_num

    def display(self):
        '''Tell my details.'''
        "Name : ", self.name, ", Mobile number: ", self.mob_num


# defining class Teacher which is child class of College
class Teacher(College):

    def __init__(self, name, mob_name, salary):
        College.__init__(self, name, mob_name)
        self.salary = salary

    def display(self):
        College.display(self)
        print "Name : ", self.name, ", Mobile number: ", self.mob_num, ", Salary:", self.salary


# defining class Student which is child class of College
class Student(College):

    def __init__(self, name, mob_num, grade):
        College.__init__(self, name, mob_num)
        self.grade = grade

    def display(self):
        College.display(self)
        print "Name : ", self.name, ", Mobile number: ", self.mob_num, ", Grade:", self.grade


t = Teacher('Python Sir', 1235634, 20000)
s = Student('James', 567765, 'A')
t.display()
s.display()

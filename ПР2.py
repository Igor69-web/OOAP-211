class Student:
    def __init__(self, name, data, phone, mail, university, gender, faculty, special, grade, group='ADEU-211'):
        self.name = name
        self.data = data
        self.phone = phone
        self.mail = mail
        self.university = university
        self.gender = gender
        self.faculty = faculty
        self.special = special
        self.grade = grade
        self.group = group

    def display(self):
        return self.name, self.grade, d[self.grade]

    def deduction(self):
        print("Отчислен студент " + str(self.display()))

    def __del__(self):
        if self.grade == 2:
            self.deduction()
d = {2: 'Задолжник', 4: 'Ударник', 5: 'Отличник'}
s1 = Student("Лобанов", "01.01.2001", "88005553535", "lob_123@gmail.com", "МГПУ", "м", "11", "211", 2)
s2 = Student("Петров", "01.01.1999", "8800235167", "petrov@gmail.com", "МГПУ", "ж", "11", "211", 5)
if s1.grade > s2.grade:
    s2.deduction()
elif s1.grade < s2.grade:
    s1.deduction()
else:
    print("МОЛОДЦЫ!")

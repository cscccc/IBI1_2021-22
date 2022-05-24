class Staff:
    def __init__(self, first_name, last_name, age, location, role):
        self.name = first_name + last_name
        self.age = age
        self.location = location
        self.role = role
    def inf(self):
        print(self.name,  self.location, self.role)
Staff1 = Staff('Rob', 'Young', '24','Edingburg', 'Teacher')
Staff1.inf()

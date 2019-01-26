class Student(object):
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.mark = []

    def average(self):
        return sum(self.marks) / len(self.mark)

    @classmethod
    def friend(cls, friend_name, origin, **kwargs):
        return cls(friend_name, origin.school, **kwargs)


class WorkingStudent(Student):
    """docstring for WorkingStudent."""
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


player1 = WorkingStudent("yang", "SHU", job_title="SWE", salary=1500)
friend = player1.friend("anna", player1,salary=1500, job_title="SWE")

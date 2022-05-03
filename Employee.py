from Person import Person


class Employee(Person):

    JOB_STATUS = 'Employed'

    def __init__(self, name, gender, food, colour, job):
        super().__init__(name, gender, food, colour)
        self._job = job

    # getter property
    @property
    def job(self):
        return self._job

    # setter property
    def set_job(self,job):
        self._job = job

    # Name and gender not needed. super in
    def __str__(self):
        var = super().__str__()
        return var + ' Job: ' + self._job

    def apply_raise(self):
        self._pay = int(self._pay * 1.2)


e1 = Employee('Jen', 'Female', 'Chips', 'green', 'teacher')

print(e1)


class Employee(object):
    """
    A salaried employee.

    """
    def __init__(self, name, salary):
        """
        Initialise a new Employee instance.

        Parameters:
            name (str): The employee's name.
            salary (float): The employee's annual salary.

        """
        self._name = name
        self._salary = salary

    def get_name(self):
        """
        (str) Return the name.

        """
        return self._name

    def wage(self):
        """
        (float) Return the forgnightly wage.

        """
        return self._salary/26


class Worker(Employee):

    def __init__(self, name, salary, manager):
        super().__init__(name, salary)
        self._manager = manager

    def get_manager(self):
        return self._manager

class Executive(Employee):
    
    # def __init__(self, name, salary, bonus):
    #     super().__init__(name, salary)
    #     self._bonus = bonus

    def wage(self):
        return super().wage() + self._bonus / 24

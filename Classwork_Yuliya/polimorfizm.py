class Person:
    def __init__(self, name):
        self.name = name

    def activity(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def activity_and_title(self):
        print(f"{self.name} - {self.activity()}")


class UkrainePresident(Person):
    def activity(self):
        return "now a handsome man"


class CommanderInChief(Person):
    def activity(self):
        return "a specialist in creating boilers"


class RussiaPresident(Person):
    def activity(self):
        return "Politico: loser of the year"


Zelensky = UkrainePresident("Volodymyr Zelensky")
Zaluzhny = CommanderInChief("Viktor Zaluzhny")
Putin = RussiaPresident("Vladimir Putin")

people = [Zelensky, Zaluzhny, Putin]

for person in people:
    person.activity_and_title()















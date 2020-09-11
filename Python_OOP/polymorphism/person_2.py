class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return self.name + " " + other.surname


class Group:
    def __init__(self, name, people=None):
        if people is None:
            people = []
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __str__(self):
        members = ', '.join(str(x) for x in self.people)
        return f'Group {self.name} with members {members}'

    def __add__(self, other):
        result = []
        final = []
        for x in self.people:
            result.append(x)
        for x in other.people:
            result.append(x)

        for idx, x in enumerate(result):
            item = f'Person {idx}: {x}'
            final.append(item)

        return final

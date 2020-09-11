class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name: str, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(self.name + other.name, self.people + other.people)

    def __len__(self):
        return len(self.people)

    def __getitem__(self, ind):
        return f'Person {ind}: {self.people[ind]}'

    def __str__(self):
        return f'Group {self.name} with members {", ".join(str(x) for x in self.people)}'


import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Emil", "Grigorov")

    def test_custom_str(self):
        result = str(self.person_1)
        self.assertIn("Emil", result)
        self.assertNotIn("Person", result)
        self.assertEqual(result, "Emil Grigorov")

    def test_custom_add(self):
        person_2 = Person("Test", "Testov")
        person_3 = self.person_1 + person_2
        self.assertEqual(person_3.name, "Emil")
        self.assertEqual(person_3.surname, "Testov")


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("Emil", "Grigorov")
        self.person_2 = Person("Second", "Person")
        self.group = Group("test", [self.person_1, self.person_2])

    def test_custom_len(self):
        result = len(self.group)
        self.assertEqual(result, 2)

    def test_custom_add(self):
        person_3 = Person("Third", "Third")
        group_2 = Group("test2", [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_custom_get_item(self):
        result = self.group[1]
        self.assertIn("Second", result)

    def test_custom_get_item_invalid_index(self):
        with self.assertRaises(IndexError):
            result = self.group[2]

    def test_custom_str(self):
        result = str(self.group)
        self.assertIn("Group", result)
        self.assertIn("Emil", result)
        self.assertIn("Second", result)
        self.assertNotIn("Third", result)

    def test_set_attributes(self):
        self.assertEqual(self.group.name, "test")
        self.assertEqual(len(self.group.people), 2)


if __name__ == "__main__":
    unittest.main()

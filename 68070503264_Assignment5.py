class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.marks = {}

    def add_mark(self, subject, score):
        if subject in self.marks:
            self.marks[subject] = score
            print(f"Updated {subject} = {score}")
        else:
            self.marks[subject] = score
            print(f"Added {subject} = {score}")

    def display_marks(self):
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"{subject}: {score}")

    def average(self):
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        count = len(self.marks)
        return total / count

student1 = Student("Alice", 16)


student1.display_info()


student1.add_mark("Math", 90)
student1.add_mark("Science", 85)


student1.display_marks()


avg = student1.average()
print(f"Average Score: {avg:.2f}")
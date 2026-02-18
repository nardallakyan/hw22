# homework 26
# class Triangle:
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError("Erankyan koxmery petq e linen drakan tver")
#
#         if a + b <= c or a + c <= b or b + c <= a:
#             raise ValueError("Trvats erankyan koxmerov erankyun anhnar e")
#
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def sides(self):
#         return self.a, self.b, self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = self.perimeter() / 2
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
#     def type_by_sides(self):
#         if self.a == self.b == self.c:
#             return "Havasarakoxm erankyun"
#         elif self.a == self.b or self.a == self.c or self.b == self.c:
#             return "Havasarasrun erankyun"
#         else:
#             return "Ankanon erankyun"
#
#     def is_right_triangle(self):
#         sides = sorted([self.a, self.b, self.c])
#         return math.isclose(sides[0] ** 2 + sides[1] ** 2,sides[2] ** 2)
#
#     def angles(self):
#         A = math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)))
#         B = math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c)))
#         C = 180 - A - B
#         return A, B, C
#
#     def inradius(self):
#         return self.area() / (self.perimeter() / 2)
#
#     def circumradius(self):
#         return (self.a * self.b * self.c) / (4 * self.area())


# 1 oop


# import random
# class Student:
#     def __init__(self, name, group, grade):
#         self.name = name
#         self.group = group
#         self.grade = grade
#
#     def average_grade(self): return sum(self.grade) / len(self.grade)
#
#     def __repr__(self): return f"{self.name}, группа {self.group}, средний балл: {self.average_grade():.2f}"
#
# #from faker.proxy import Faker
# # for i in range(1,11):
# #    faker = Faker(locale='hy-am')
# #    print(i,faker.name())
# names = ["Հերմինե Ազանյան", "Մանվել Ալաջաջյան", "Վերոնիկա Ղազարյան", "Ռաիսա Ադուլյան", "Արտաշես Պապիկյան",
#          "Իննա Զոհրաբյան", "Սահակ Թևոսյան", "Թաթուլ Ազատյանց", "Ջուլիետա Աբրահամյան", "Վահագն Աթբաշյան"]
# students = []
# for i in range(10):
#    grades = [random.randint(2, 5) for _ in range(5)]
#    students.append(Student(names[i], random.randint(101, 105), grades))
#
# print(students)


#hw 1 homework 28
# class Animal:
#     def eat(self):
#         return "Animal is eating..."
#
#     def sleep(self):
#         return "Animal is sleeping..."
#
#
# class Bird(Animal):
#     def eat(self):
#         return "Bird is pecking at its food..."
#
#     def fly(self):
#         return "Bird is flying..."
#
#
# class Fish(Animal):
#     def swim(self):
#         return "Fish is swimming..."
#
#
# bird = Bird()
# fish = Fish()
#
# print(bird.eat())
# print(bird.sleep())
# print(bird.fly())
#
# print(fish.eat())
# print(fish.sleep())
# print(fish.swim())


#hw 29
# class MyShows:
#     def __init__(self, name, platform, year, episode=1, rating=None, actors=None):
#
#         if not isinstance(name, str): raise ValueError("seriali anunyny petq e lini text")
#         if not isinstance(platform, str): raise ValueError("hartaky petq e lini text")
#         if not isinstance(year, int): raise ValueError("taretivy amboxj tiv")
#         if not isinstance(episode, int) or episode < 1: raise ValueError("seriali hmary amboxj tiv")
#         if rating is not None and (not isinstance(rating, int) or not (1 <= rating <= 10)):
#             raise ValueError("gnahatakany  1 - 10 mijakyqyum")
#         if not isinstance(actors, list): raise ValueError("derasanery linen list")
#
#
#         self.__name = name
#         self.__platform = platform
#         self.__year = year
#         self.__episode = episode
#         self.__rating = rating
#         self.__actors = actors
#
#
#     def get_name(self): return self.__name
#     def get_platform(self): return self.__platform
#     def get_year(self): return self.__year
#     def get_episode(self): return self.__episode
#     def get_rating(self): return self.__rating
#     def get_actors(self): return self.__actors

#
#     def set_episode(self, ep):
#         if isinstance(ep, int) and ep > 0:
#             self.__episode = ep
#         else:
#             raise ValueError("lini drakan amboxj tiv")
#
#     def set_rating(self, r):
#         if isinstance(r, int) and 1 <= r <= 10:
#             self.__rating = r
#         else:
#             raise ValueError("gnahatakany 1-10 mijakyqum")
#
#
#     def del_rating(self):
#         self.__rating = None
#
#
#     def add_actor(self, actor):
#         if isinstance(actor, str):
#             self.__actors.append(actor)
#         else:
#             raise ValueError("derasni anuny")
#
#     def remove_actor(self, actor):
#         if actor in self.__actors:
#             self.__actors.remove(actor)
#
#
#     def info(self):
#         return {
#             "Name": self.__name,
#             "Platform": self.__platform,
#             "Year": self.__year,
#             "Episode": self.__episode,
#             "Rating": self.__rating,
#             "Actors": self.__actors
#         }
#
# sopranos = MyShows(
#     name="The Sopranos",
#     platform="HBO",
#     year=1999,
#     episode=1,
#     rating=None,
#     actors=["James Gandolfini", "Lorraine Bracco", "Edie Falco", "Michael Imperioli"]
# )
#
# print(sopranos.info())
#
#
# sopranos.set_episode(5)
# sopranos.set_rating(10)
# sopranos.remove_actor("Lorraine Bracco")
# print(sopranos.info())


class Restaurant:
    def __init__(self, name, tables_count):
        self.name = name
        self.tables_count = tables_count
        self.reservations = {}

    def make_reservation(self, name, table_number, date):
        if date not in self.reservations:
            self.reservations[date] = 0

        if self.reservations[date] + table_number > self.tables_count:
            print("No seats available.")
        else:
            self.reservations[date] += table_number
            print(f"Reservation made for {name} at {date}.")

    def order_food(self, *items):
            print(f"Order with {', '.join(items)} placed!")

    def order_food(self, *items):
            print(f"Order with {', '.join(items)} placed!")



class FastFoodRestaurant(Restaurant):
    def __init__(self, name):
        super().__init__(name, 0)

    def make_reservation(self, name, table_number, date):
        print("We don't take reservations.")














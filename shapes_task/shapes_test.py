from circle import Circle
from triangle import Triangle

c_1 = Circle(1)
c_2 = Circle(2)
c_3 = Circle(0.5)
c_4 = Circle(4)

c_list = [c_2, c_1, c_4, c_3]
print(c_list)
c_list.sort(key=lambda x: x.get_area())

print(c_list)

t_1 = Triangle(0, 0, 2, 3, 11, 15)
t_2 = Triangle(0, 0, 2, 3, 11, 15)
t_3 = Triangle(4, 13, 2, 3, 11, 15)

print(t_1)
print(t_1 == t_2)
print(t_1 == t_3)

from circle import Circle

c_1 = Circle(1)
c_2 = Circle(2)
c_3 = Circle(0.5)
c_4 = Circle(4)

c_list = [c_2, c_1, c_4, c_3]
print(c_list)
c_list.sort(key=lambda x: x.get_area())

print(c_list)

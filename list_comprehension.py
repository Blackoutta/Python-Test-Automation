my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
multiply_list = [x + 1 for x in range(5)]

# even_list = [x for x in range(30) if x % 2 == 0]
# print(even_list)

people = ["John", "RoY ", "AlICe ", " WhIety"]
normalized_people = [person.strip().title() for person in people]
print(normalized_people)

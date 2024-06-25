grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

st1 = sum(grades[0]) / len(grades[0])
st2 = sum(grades[1]) / len(grades[1])
st3 = sum(grades[2]) / len(grades[2])
st4 = sum(grades[3]) / len(grades[3])
st5 = sum(grades[4]) / len(grades[4])
average_ratings = [st1, st2, st3, st4, st5]
score = list(average_ratings)
sorted_students = list(students)
sorted_students.sort()
students_journal = dict(zip(sorted_students, score))
print(students_journal)







#scores = sum(grades.index()) // len(grades)
#numbers = [4, 8, 6, 5, 3, 2]
#average = sum(numbers) / len(numbers)
#print(average) # 4.666666666666667
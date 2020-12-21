import io

all_data = []
with io.open('students.txt', encoding='utf-8') as students:
    for line in students:
        all_data.append(line.replace('\n', '').split(' - '))

all_data = sorted(all_data, key=lambda x: x[0])

sorted_students = open('sorted_students.txt', 'w', encoding='utf-8')
for student in all_data:
    sorted_students.write(student[0] + ' - ' + student[1] + '\n')

sorted_students.close()

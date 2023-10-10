
class student:

   def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # sort the list of student in descending order of cgpa
  sorted_students = sorted(student_list,
          key=lambda student: student.cgpa, 
                              reverse=True)
# syntax -lambda arg:exp
  return sorted_students


  # example usage:
students =  [
   student("kalai", "A123", 7.8),
   student("varsha", "A124", 8.9),
   student("bhavani", "A125", 9.1),
   student("shobi", "A126", 9.9),
  ]

sorted_students = sort_students(students)

# print the sorted list of studentS
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
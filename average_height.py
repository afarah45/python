# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#Calculate Average height using for loop

total_height = 0
total_students = 0
for h in student_heights:
  total_height += h  
  total_students  += 1 
print(total_height)
print(total_students)
average_height = round(total_height/total_students)
print(average_height)
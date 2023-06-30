"""Write a Python code to input a marks and print the message according to the following rules:-
Marks above 90 : "Excellent"
Marks above 70 but less than 90 : "Good"
Marks above 40 but less than 70 : "Needs Improvement"
Marks below 40 : "Fail"""
x = int(input("Please enter a value"))
if (x>=90):
  print("You have achieved excellent marks")
elif (x>=70):
  print("You have achieved good marks")
elif (x>=40):
  print("Your marks need improvment")
else:
  print("You have failed")
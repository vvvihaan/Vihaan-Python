"""Write a python code to take input of marks in 5 subjects and print the total and the average."""
eng = float(input("Input your marks for english", ))
maths = float(input("Input your marks for maths", ))
history = float(input("Input your marks for history", ))
software = float(input("Input your marks for software", ))
pdhpe = float(input("Input your marks for pdhpe", ))
total = (eng+maths+history+software+pdhpe)
average = total/5
print("Total = ",total,"\nAverage = ",average)
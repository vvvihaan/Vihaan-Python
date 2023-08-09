"""Write a program that accepts a string and checks if it is a valid IP address.
192.168.1.1

0-255 
""" 
isValid=False #flag variable to store the status
x = input("Enter a valid ip," )
ip = x.split(".")
ip_length = len(ip)
# print(ip)
for i in range(ip_length):
   element=int(ip[i])
   if (element >= 0) and (element <= 255):
     isValid=True
   else:
     isValid=False
     break
     
if isValid == True:
  print("IP address is valid")
else:
  print("IP address is not valid")
     
  
  

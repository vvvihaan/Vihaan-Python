a = int(input("Enter side"))
b = int(input("Enter side"))
c = int(input("Enter side"))

def triangle_type(a:int,b:int,c:int):
  if (a == b and b == c and c == a):
    return "Equillateral"
  elif (a == b or b == c or c == a):
    return "Isosceles"
  else:
    return "Scalene"

x = triangle_type(a,b,c)
print(x)
    










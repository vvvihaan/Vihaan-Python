"""Write a python code for a Castco Store! Where you buy Pizzas for $20 each, Burgers for $25 each,  Coke for $10 each and Packets of Chips for $5 each. Calculate and print the final amount."""
pizza = int(input("How many  pizzas would you like", ))
pizza2 = pizza*20
coke = int(input("How many ,cokes would you like", ))
coke2 = coke*10
burgers = int(input("How many burgers would you like", ))
burger2 = burgers*25
chips = int(input("How many chip packets  would you like", ))
chip2 = chips*5
print("This is the final amount","$",pizza2+coke2+burger2+chip2)
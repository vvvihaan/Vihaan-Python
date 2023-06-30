"""Sanjeev went to the mall and bought 5 pair of jeans for $50 each, 10 T-Shirts for $ 20 each, 2 Belts for $10 each and 2 pair of shoes for $70 each.
Write a python code to calculate the total amount and give a discount of 20%. and 30% cashback"""
Jen = 50
shirt = 20
belt = 10
shoe = 70
Total = ((Jen*5)+(shirt*10)+(belt*2)+(shoe*2))
discounted_total = 20/100*Total
cashback = 30/100*discounted_total
print("Discounted price =","$",discounted_total,"Cashback = ","$",cashback)
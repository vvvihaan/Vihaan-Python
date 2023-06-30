"""Vihaan goes to a Kmart store to buy some toys, he bought 1 set of skates for $40, 4 set of Avengers character for $10 each, a helmet for $50 and 5 Barbie Sets (to gift sisters) for $30 each. 
If he was allowed a discount of 20%, Write a python code to print the final amount"""
skates = 40
Avg = 10
helm = 50
bar = 30
Total = (skates+(Avg*4)+helm+(bar*30))
discount = 20/100*Total
new_total =Total - discount
print("Here is your original total",Total,"Here is your discounted total",new_total)
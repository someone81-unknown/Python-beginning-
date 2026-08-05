print("price is 45 dollar")
print("tax is 5%")
print("you're discounted 10 dollars for loyalty")
price=45
tax=0.05
discount=10
tax_money=price*0.05
total_price=price+tax_money-discount
print(total_price)
print(
f"""
{"="*60}

TOTAL:{total_price}

DISCOUNT:{discount}

TAX:{tax_money}
                   
                   THANKS FOR COMING!

{"="*60}
""")

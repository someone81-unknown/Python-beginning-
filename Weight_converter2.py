weight=float(input("what is your weight?\n "))
unit=input(f" kilograms(K) or pounds(l)")
kg_weight=weight/2.20462
pound_weight=weight*2.20462
if unit.upper()=="L":
	print(f"{kg_weight}{" kilograms"}")
elif unit.upper()=="K":
	print(f"{pound_weight}{" pounds"}")

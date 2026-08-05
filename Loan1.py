has_good_credit=False
has_bad_credit =True
price=1000000
d_p_f_g_c=price*0.1
if has_good_credit:
	print(f'{d_p_f_g_c}{" dollars"}')
elif has_bad_credit:
	down_payment=price*0.2
	print(f'${down_payment} dollars')
else:
	print(f"""sorry we cant give you a house!
	
{"*"*60}
""")

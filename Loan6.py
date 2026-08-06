good_credit=False
no_criminal_record=True
if good_credit or not no_criminal_record:
	print("you're eligible for this!")
	print(f"""
{"*"*60}

                          APPLY HERE!

{"*"*60}
""")
else:
	print("go from here")

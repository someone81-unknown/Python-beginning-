started=False
while True:
    command=input("> ").lower()
    if command=="start":
    	if not started:
    		print("started already")
    	else:
    		started=True
    		print("car started") 
    elif command=="stop":
    	if not started:
    		print(" car stopped")
    	else:
    		started=True
    		print("already stopped")
    elif command=="help":
    	print(f"""
start--to start the car
stop-- to stop the car
quit--to quit the menu
    	""")
    elif command=="quit":
    	break
    else :
    	print("sorry, i don't understand that. try help")

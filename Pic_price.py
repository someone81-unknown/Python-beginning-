name=input("what is your name, sir? ")
country=input("which country are you from? ")
company=input("what's your company name? ")
image_type=input("what type of images do you want? ")
image_style=input("what style of images do you want? ")
resolution=input("what resolution do you want ,sir? ")
number_of_images=int(input("how many images do you want in one month? "))
cost=float(0.36)
print("cost per image is 0.36 dollars")
print("so the monthly cost is "+str(int(number_of_images)*cost)+ " dollars")
receipt=input("do you want a receipt?" )
total_cost=(number_of_images*cost)
print(f""" 
{'*'*60} 

                             AI MAX
                             
                             
{"*"*60}                        

COMPANY:                {company}

COUNTRY:                  {country}

IMAGES:                     {number_of_images}

RESOLUTION:             {resolution}
{"-"*60}

TOTAL COST:             {str(total_cost) + " dollars"}


                                    {'*'*10}
""")

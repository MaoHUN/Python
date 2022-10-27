import random
#Variables
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@!#;%/?:.-_"
#Method
user_for = lower_case + upper_case + number + symbols
input_a = int(input("How many charter do you need? "))
#Generate password
def generate() :
    if input_a <= 32 :
        pwd = "".join(random.sample(user_for, input_a))
        print("Your password is: " + pwd)
    else:
        print("higher then 32")
# Is it number? yes -> generate password | no -> error
def is_it_number():
    
    if type(input_a) == int :
                    generate()
    else:
                    print("Not integer!!!!")
                    return 0

is_it_number()

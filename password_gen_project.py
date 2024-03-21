import random
latters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w',
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','=']
print("\t\t -:Wellcome to Password generator:-")
n_latter = int(input("How many latter you want for your password:"))
n_number = int(input("How many number you want for your password:"))
n_symbol = int(input("How many symbol you want for your password:"))
password = " "
for a in range(1,n_latter+1):
    char = random.choice(latters)
    password = password+char

#print(password)
for a in range(1,n_number+1):
    char = random.choice(numbers)
    password = password+char

#print(password)
for a in range(1,n_symbol+1):
    char = random.choice(symbols)
    password = password+char
print("Your Password is Ready:"+password)

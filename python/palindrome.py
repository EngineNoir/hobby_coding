number = input("Input the number: ")
number_as_int = int(number)

i = 1
is_palindrome = True

while i < len(number)/2 + 1:
    number_from_top = int(number_as_int/(10**(len(number)-i))) % 10 
    number_from_bottom = int((number_as_int % (10**i)) / (10**(i-1)))
    
    i += 1
    if number_from_top != number_from_bottom:
        is_palindrome = False


if is_palindrome:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")

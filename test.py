dogs = []
dogs.append("Deutsche Schaefferhund")
dogs.append("Labrador")
print(dogs)
dogs.reverse()
print(dogs)
dogs.sort()
print(dogs)

num = 1 + 2 * 3 / 4.0
print("num =", num)

lotsofhellos = "hello"*10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
all_numbers.sort()
print(all_numbers)

print("2**5 = 2^5 = %d" % 2**5)
# Any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string.
mylist = [1,2,3]
print ("A list: %s" % mylist)
print("len(mylist) = ", len(mylist))
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

string2 = "string!"
print("len(string2) = ", len(string2))
print("string2.count('!') = ", string2.count('!'))
print("string2[2:len(string2)] = ", string2[2:len(string2)])
# ends substr at index: len(string) - 1

if string2.index('!') == len(string2) - 1:
	print("That string ends in an exclamation point!")
else:
	print("That string does not end in an exclamation point.")

phrase = "Integers in hex representation (lowercase/uppercase)"
phrase_parsed1 = phrase.split()
print(phrase_parsed1)
phrase_parsed2 = phrase.split(" ")
print(phrase_parsed2)
phrase_parsed3 = phrase.split("a")
print(phrase_parsed3)

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

import math

# helper fns

def is_prime(num):
	for x in range(2, int(num)):
		if (num % x == 0):	return False
	return True

def lgst_prime_factor(num):

	for x in range(num - 1, 1, -1):
		if (num % x == 0  and  is_prime(x)):
			return x


num = 600851475143
# print(lgst_prime_factor(num))

num_sqrt = math.floor(math.sqrt(num))
# print(num_sqrt)

prime_factors = []

for x in range(num_sqrt,1,-1):
	if (num % x == 0):
		if is_prime(x):
			prime_factors.append(x)
		if is_prime(num/x):
			prime_factors.append(num/x)
prime_factors.sort()
print("prime_factors (ascending):", prime_factors)
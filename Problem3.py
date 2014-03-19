# helper fns

def is_prime(num):
	for x in range(2, num):
		if (num % x == 0):	return False
	return True

def lgst_prime_factor(num):

	for x in range(num - 1, 1, -1):
		if (num % x == 0  and  is_prime(x)):
			return x


num = 6008#51475143
# print(lgst_prime_factor(num))

factor = 3; 
while(num > 1):
	if(num % factor == 0):
		num/=factor;
	else:
		factor += 2; #skip even numbrs
print(factor);

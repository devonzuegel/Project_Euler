sum = 0
last_fib_num = 1
curr_fib_num = 2

while curr_fib_num <= 4000000:	  #  <= 4 million

	if (curr_fib_num % 2 == 0):
		sum += curr_fib_num
		print(curr_fib_num)

	curr_fib_num += last_fib_num
	last_fib_num = curr_fib_num - last_fib_num;

print(sum)
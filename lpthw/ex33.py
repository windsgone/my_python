def add_numbers(top, step):
	i = 0
	numbers = []

	# for i in range(top): use for-loop

	while i < top:
		print "At the top is %d" % i
		numbers.append(i)

		i += step
		print "numbers now: ", numbers
		print "At the bottom is %d" % i 

	print "The numbers: "

	for num in numbers:
		print num
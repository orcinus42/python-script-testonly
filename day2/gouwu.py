#!/usr/bin/env python
#
products = ['car','iphone','bike','coffee','pythoncourse']
prices = [350000,4800,800,33,5800]
shopping_list = []

salary = int(raw_input("Your current salary:"))

while True:
	print "Sale list:"
	for p in products:
		print p, prices[products.index(p)]
	option = raw_input("what do you want to buy?:").strip()
	if len(option) == 0:continue
	if option in products:
		p_price = prices[products.index(option)]
		if salary > p_price :
			print 'Adding \033[32;1m%s\033[0m into shopping list.' % option
			shopping_list.append(option)
			salary = salary - p_price
			print "You current balance:\033[31;1m%s\033[0m" % salary
			continue
		else:
			print "\033[33;1mSorry,you cannot afford to buy %s\033[0m" % option
			if salary < min(prices):
				print "\033[33;1mToo poor to buy anything from us,fuck off!\033[0m"
				break







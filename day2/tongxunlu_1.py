#!/usr/bin/env python
#
contact_dic = {}
with open ('contact.txt') as f:
	for i in f.readlines():
		line = i.strip().split()
		contact_dic[line[0]] line[1:]
print contact_dic.keys()

choice = raw_input("Do you want execute CRUD operation?(y/n) ").strip()
if choice == 'Y' or choice == 'y':
	action = raw_input("Do you want to choose which one operation?(A=Add/U=Update/D=Detete/R=Recove) ").strip()
	if action == 'A':
		adduser = raw_input("Please enter the user name you want to add: ").strip()
		phone = raw_input("Please enter the phone number you want to add: ").strip()
		company = raw_input("Please enter the company you want to add: ").strip()
		email = raw_input("Please enter the e-mail you want to add: ").strip()
		print adduser,phone,company,email
		if contact_dic.ha_key(adduser):
			print 'User already exist !'
		else:
			with open('contacts.txt','a') as f:
				f.write(adduser + ' ' + phone + ' ' + company + ' ' + email + '\n')
	elif action == 'U':
		#print 'OK'
		update_user = raw_input("Please enter the user name you want to update: ").strip()
		print update_user
		if contact_dic.has_key(update_user):
			print contact_dic[update_user]

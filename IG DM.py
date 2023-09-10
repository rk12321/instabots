from instadm.instadm import InstaDM

if __name__ == '__main__':
	# Auto login
	insta = InstaDM(username='gymfeaks', password='Password1', headless=False)
	
	# Send message
	insta.sendMessage(user='itsreetik', message='Hey there')
	
	# Send message
	#insta.sendGroupMessage(users=['user1', 'user2'], message='Hey !')

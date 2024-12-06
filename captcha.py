# Python program to automatically generate CAPTCHA and
import random

# Returns true if given two strings are same
def checkCaptcha(captcha, user_captcha):
	if captcha == user_captcha:
		return True
	return False

# Generates a CAPTCHA of given length
def generateCaptcha(n):
	
	# Characters to be included
	chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	
	# Generate n characters from above set and
	# add these characters to captcha.
	captcha = ""
	for i in range(n):
		captcha =captcha+ chrs[random.randint(0, 61) ]
	return captcha

# Generate a random CAPTCHA
captcha = generateCaptcha(6)
print(captcha)

# Ask user to enter a CAPTCHA
print("Enter above CAPTCHA:")
usr_captcha = input()

# Notify user about matching status
if (checkCaptcha(captcha, usr_captcha)):
	print("CAPTCHA Matched")
else:
	print("CAPTCHA Not Matched")


from sys import argv

script, user_name, user_last_name = argv
prompt = '""""""">!@# '
 
print ("Hi %s, I'm the %s script." % (user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = raw_input(prompt)

print("What is your last name?")
user_last_name = raw_input(prompt)

print("Where do you live %s?" % user_name)
lives = raw_input(prompt)

print("What kind of computer do you have")
computer = raw_input(prompt)

print("""
Alright, so you said %r about liking me,
Your last name is %r
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, user_last_name, lives, computer) )
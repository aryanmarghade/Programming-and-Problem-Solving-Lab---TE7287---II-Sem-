string = input()
l = len(string)
f = True
for i in range(l):
	if string[i] != string[l - 1 - i]:
		f = False
		break
if f:
	print("Palindrome")
else:
	print("Not a Palindrome")

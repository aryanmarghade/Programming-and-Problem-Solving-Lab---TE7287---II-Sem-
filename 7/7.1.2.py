a,b,c =input().split()
num=[a,b,c]
for i in range(3):
	for j in range(3):
		for k in range(3):
			if(i != j and i != k and j != k):
				print(num[i]+num[j]+num[k])

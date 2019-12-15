d = {'a':5,'b':4,'c':3,'d':2,'e':1}
s = list(d.keys())
for i in range(len(s)):
	for j in range(i,len(s)):
		if d[s[j]] < d[s[i]]:
			c = s[j]
			s[j] = s[i]
			s[i] = c
print(s)

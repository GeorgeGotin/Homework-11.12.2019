d = {'a':1,'b':2}
s = list(d.keys())
m = s[0]
for i in s:
	if d[i] > d[m]:
		m = i
print(m)

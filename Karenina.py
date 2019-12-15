import re  


def sort(d):
	s = list(d.keys())
	for i in range(len(s)):
		for j in range(i,len(s)):
			if d[s[j]] > d[s[i]]:
				c = s[j]
				s[j] = s[i]
				s[i] = c
	return s

book = open("karenina.txt")  
text = book.read() 
f =dict({})
for word in re.split("\W+", text):  
    w = word.strip().lower() 
	if f.get(w,'#') == '#':
		f[w] = 1
    else:
		f[w] = f[w] + 1
s = sort(f)
for i in range(len(s)):
	print('{1}. {2} - {3} times'.format(i,s[i],d[s[i]]))

		

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
 if len(w) <= 3:
	 continue 
 if f.get(w,'#') == '#':
  f[w] = 1
 else:
  f[w] = f[w] + 1
s = sort(f)
for i in range(100):
 print('{}. {} - {} times'.format(i+1,s[i],f[s[i]]))
for i in range(100,-1):
 print('{}. {} - {} times'.format(i+1,s[i],f[s[i]]))

		

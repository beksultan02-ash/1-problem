import re
def find(s):
     charRe  = re.compile(r'[^a-zA-Z0-9.]')
     s = charRe.search(s)
     return not bool(s)


s= input()
print (find(s) )
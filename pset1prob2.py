s = 'azcbobobegghakl'
bob = 0
for i in range(len(s)-2):
    if s[i:i+2] + s[i+1] + s[i+2] == 'bob':
      bob += 1
print(bob)
   
    
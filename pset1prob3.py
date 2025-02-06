s = 'azcbobobegghakl'

alpha = ''
last_al = ''
gr_alpha = s[0]
for i in range(len(s)-1):
    if s[i] <= (s[i+1]):
        alpha += (s[i])
        last_al = (s[i+1])    
        if len(alpha)+1 > len(gr_alpha):
            gr_alpha = alpha + last_al
    else:
        alpha = ''
print(gr_alpha)
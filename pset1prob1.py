s = 'azcbobobegghakl'
vowels = 'aeiou'
count = 0

for letter in s:
    for vowel in vowels:
        if letter == vowel:
            count += 1
print("Number of vowels: "+ str(count))
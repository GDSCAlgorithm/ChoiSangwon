from collections import Counter

name = input()
freq = Counter(name)

odd_count = 0
mid_char = ''

for char, count in freq.items():
    if count % 2 != 0:
        odd_count += 1
        mid_char = char

if odd_count > 1:
    print("I'm Sorry Hansoo")
    exit()

first_half = ''
for char in sorted(freq.keys()):
    first_half += char * (freq[char] // 2)

palindrome = first_half + mid_char + first_half[::-1]
print(palindrome)


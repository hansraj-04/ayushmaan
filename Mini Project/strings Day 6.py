# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for ch in s:
#     if ch in vowels:
#         count += 1

# print("Number of vowels:", count)


# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0

# for ch in s:
#     if ch.isalpha() and ch not in vowels:
#         count += 1

# # print("Number of consonants:", count)

# s = input("Enter a string: ")
# rev = ""

# for ch in s:
#     rev = ch + rev   
# print("Reversed string:", rev)


# s = "imlove Marvel"
# s1= " "

# for ch in s:
#     if ch.isspace():   
#         s1 += "-"  
#     else:
#         s1 += ch

# print("Original:", s)
# print("Modified:", s1)


# s = input("Enter a string: ")
# result = s.title()
# print("Modified string:", result)


# s = input("Enter a string: ")
# words = s.split()
# result = " ".join(w[0].upper() + w[1:].lower() for w in words)
# print(result)

# s = input("Enter a sentence: ")
# words = s.split()

# longest = ""
# for w in words:
#     if len(w) > len(longest):
#         longest = w

# print("Longest word:", longest)
# print("Length:", len(longest))

# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# s = input("Enter a string: ")
# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print("String after removing duplicates:", result).

# s = input("Enter a string: ")
# freq = {}

# for ch in s:
#     if ch.isalpha():       
#         freq[ch] = freq.get(ch, 0) + 1

# max_char = ''
# max_count = 0
# for ch, count in freq.items():
#     if count > max_count:
#         max_char = ch
#         max_count = count

# print("Most frequent character:", max_char)
# print("Frequency:", max_count)

# pwd = input("Enter password: ")

# if (len(pwd) >= 8 and any(c.isupper() for c in pwd) 
#     and any(c.islower() for c in pwd) 
#     and any(c.isdigit() for c in pwd) 
#     and any(c in "!@#$%^&*()-_+=" for c in pwd)):
#     print("Strong password ")
# else:
#     print("Weak password ")

# password = input("Enter password: ")

# special_chars = "!@#$%^&*()_+-="

# if len(password) < 6:
#     print("Password too short")
# elif not any(c.isupper() for c in password):
#     print("Add at least one uppercase letter")
# elif not any(c.islower() for c in password):
#     print("Add at least one lowercase letter")
# elif not any(c.isdigit() for c in password):
#     print("Add at least one number")
# elif not any(c in special_chars for c in password):
#     print("Add at least one special character")
# else:
#     print("Valid password")



s = input("Enter a string: ")
# Remove spaces and convert to lowercase for a fair check
s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
i = 0
j = len(s_clean) - 1
flag = 0
while i < j:
    if s_clean[i] != s_clean[j]:
        flag = 1
        break
    i += 1
    j -= 1
if flag:
    print("Not a palindrome")
else:
    print("Palindrome")

















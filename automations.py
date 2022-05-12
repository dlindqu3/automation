import re 

#handle regex, one function for phone numbers, one for emails 

#valid number: 123-456-7890

with open("./assets/potential-contacts.txt") as f:
    text_from_file = f.read()

# pattern = r'(\(?\d{3}\)?[\s-.]?\d{3}[\s-.]?\d{4})'

pattern1 = re.compile(r'\d{3}-\d{3}-\d{4}')
pattern2 = re.compile(r'\(\d{3}\)\d{3}-\d{4}')
pattern3  = re.compile(r'\d{3}.\d{3}.\d{4}')
phone_results1 = re.findall(pattern1, text_from_file)
phone_results2 = re.findall(pattern2, text_from_file)
phone_results3 = re.findall(pattern3, text_from_file)

str1 = "\n".join(phone_results1)
str2 = "\n".join(phone_results2)
str3 = "\n".join(phone_results3)

str4 = str1 + str2 + str3
str4 = set(str4)

str5 = ''

for item in str4: 
  str5 += item 
# print(phone_results1)

f = open("./assets/phone_numbers.txt", "a")
f.write(str5)
f.close()

f = open("./assets/phone_numbers.txt", "r")
print(f.read())


#return 112 lines of numbers 
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
divider = 40*'='
passwords = {'bob':'123','ann':'pas123',
                  'mike':'password123',
                  'liz':"pass123"}

print(divider)
# LOG IN
print('Welcome to the app. Please log in:')

mod = True
while mod:
    user = input('USERNAME: ')
    password = input('PASSWORD:  ')

    if passwords.get(user,'0') != password:
        print('Incorrect username or password, try it again')
        print(divider)
    else:
        mod = False

print('you have been successfully logged in')
print(divider)
print('We have 3 texts to be analyzed.')

# CHOICE TEXT

choice = int(input('Enter a number btw. 1 and 3 to select: '))
print(divider)

# COUNTING WORDS

text = (TEXTS[choice - 1]).split()
num_words = len(text)
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
count = 0
frequency = {}
list_lenght_words = []

while text:
    word = text.pop().strip(",'.")
    list_lenght_words.append(len(word))
    if word.istitle():
        titlecase += 1
    elif word.isupper():
        uppercase += 1
    elif word.islower():
        lowercase += 1
    elif word.isnumeric():
        numeric += 1
        count = count + int(word)



print(f'There are {num_words} words in the selected text')
print(f'There are {titlecase} titlecase words')
print(f'There are {uppercase} uppercase words')
print(f'There are {lowercase} lowercase words')
print(f'There are {numeric} numeric strings')

print(divider)

# FREQUENCY

while list_lenght_words:
    lenght = list_lenght_words.pop()
    if lenght in frequency:
        frequency[lenght] += 1
    else:
        frequency[lenght] = 1

for item in frequency.keys():
    print(item, "*"*frequency[item], frequency[item])

print(divider)
print(f'If we summed all the numbers in this text we would get: {count}')
print(divider)


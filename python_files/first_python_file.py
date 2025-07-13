print('Hello World')


# Any line that starts with '#' is a COMMENT.
# Comment lines are for humans to read, the computer won't read them
# Leave notes for yourself or the next person who might use this code.
# Well-commented code is a blessing.

# The next bit is real code. It's some instructions to the computer.
# "Print" means "write something in the terminal panel down there below"
# What would you like to print? Fill in some comment between the '' marks

print('')

# By the way, words that not instructions to the computer always need to be in ' '
#  or  " "  marks. 

# UNcomment the next line, hit Run, and see what happens
# print(Ida B. Wells)

# OK fix that line above and re-run.

# Let's mess around some more.
# Uncomment this next section:

# print('What is your name?')
# user_name = input()
# print('Ahoy there, ' + user_name)
# print('The length of your name is:')
# print(len(user_name))

# OK great, now UNcomment this next section too

# print('Please give me a whole number between 1 and 10:')
# some_number = input()
# half_number = (int(some_number)/2)
# print('Half of that is:')
# print(half_number)

# int() ?? What is that?
# A function!  A built-in piece of code that comes with Python.
# It's short for INTEGER.  You're telling the computer:
# "Hey, everything in these parentheses is a whole number."
# Before we go on, let's check out some other built-in functions at the
# official Python page:
# https://docs.python.org/3/library/functions.html

# What other built-in functions have we already used?


# The computer recognizes different types of data. 
# We've already seen an INTEGER
# A computuer can also understand a decimal number.  This data type is called a FLOAT
# Uncomment the next section and try this:

# print('Please input an odd integer:')
# odd_integer = input()
# print('You input ' + str(odd_integer))
# half_odd_integer = int(odd_integer)/2
# print('Half of that is ' + str(half_odd_integer) + ' Its data type is:')
# print(type(half_odd_integer))

# A computer can also recognize a LIST
# Uncomment and run the next TWO sections

# list_of_albums = ["Dangerously in Love",
#  "B'Day",
#  "I Am... Sasha Fierce",
#  "4",
#  "Beyoncé",
#  "Lemonade",
#  "Renaissance",
#  "Cowboy Carter"
#  ]

# for album in list_of_albums:
#     print('I love ' + album)

# Congratulations, you have read a list and run a LOOP
# Now please write and run your own list and loop below:


#################

# OK uncomment list_of_albums so we can refer to it again.
# And we'll do an IF/ELSE loop:

# favorite = "Lemonade"

# for album in list_of_albums:
#     if album == favorite:
#         print(album + ' IS MY FAVORITE!')
#     else:
#         print('I love ' + album)

###############

# Let's make our own list and save it

# This is an IMPORT statement. It imports code so common that it's bundled with Python

# import csv

# songs = [
#     'Formation',
#     'Telephone'
# ]

# Let's add a song.  There's an append METHOD.  Any LIST can have items added to it 
# by the append METHOD

# songs.append('Break My Soul')

# for song in songs:
#     print(song)
#     # There's an upper METHOD to strings
#     # any string can be made uppercase
#     print(song.upper())

# Now you add a song below


#########

# Finally, let's save our list of songs.
# we're going to use the built-in function OPEN
# we're going to use the csv MODULE we imported, and its writer function
# we're going to use a loop 
# Uncomment the next section and run it


# outfile = open('python_files/songs.csv', 'w')
# writer = csv.writer(outfile)
# for song in songs:
#     writer.writerow([song])




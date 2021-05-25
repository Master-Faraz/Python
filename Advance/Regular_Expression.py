import re

x = '''1[Late Latin programma, from Greek] : a public notice
2a: a brief usually printed outline of the order to be followed, of the features to be presented, and the persons participating (as in a public performance)
b: the performance of a program
especially : a performance broadcast on radio or television
3: a plan or system under which action may be taken toward a goal
4: CURRICULUM
5: PROSPECTUS, SYLLABUS   inin
1910510-3033
programmed or programed; inn programming or programing'''


# Meta charactors -->



# WE want to search programming in x (string)
# .      r is for RAW STRINGS doesnot skip escape sequenced ex -> \n ,\t
a = re.compile(r"programming")
b = a.finditer(x)
for i in b:
    print(i)
    print(x[456:467])           # This will print span

# Using Meta charactors -->

# WE want to search words which contains word program in x (string)
a = re.compile(r".program")
b = a.finditer(x)
for i in b:
    print(i)

# Starts with and Ends with -->

# It checks if x starts with program --> OP --> kuch nahi aaiye ga
a = re.compile(r"^program")
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r"programing$")     # It checks if x ends with programing
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r"in*")     # one I and n can occur any times (n can be zero)
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r'in+')     # one I and atleast one n
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r'in{2}')     # one I only 2 times n
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r'(in){2}')     # It creates group --> inin occurs or not
b = a.finditer(x)
for i in b:
    print(i)

# Either or

a = re.compile(r'in{2} | in')     # Either inin or in
b = a.finditer(x)
for i in b:
    print(i)
# Special Sequences -->

a = re.compile(r'\A radio')     # Starts with radio or not
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r'\b radio')  # word starts with radio or not
b = a.finditer(x)
for i in b:
    print(i)

a = re.compile(r' radio \b')  # word ends with radio or not
b = a.finditer(x)
for i in b:
    print(i)

# number --> 1910510-3033 --> seven digit - four digit
a = re.compile(r'\d{7}-\d{4}')
b = a.finditer(x)
for i in b:
    print(i)


"""

Meta Characters :
    [] A set of characters
    \ Signals a special sequence (can also be used to escape special characters)
    . Any character (except newline character)
    ^ Starts with
    $ Ends with
    * Zero or more occurrences
    + One or more occurrences
    {} Exactly the specified number of occurrences
    | Either or
    () Capture and group

Special Sequences:
    \A Returns a match if the specified characters are at the beginning of the string
    \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
    \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

    \d Returns a match where the string contains digits (numbers from 0-9)
    \D Returns a match where the string DOES NOT contain digits
    \s Returns a match where the string contains a white space character
    \S Returns a match where the string DOES NOT contain a white space character
    \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
    \W Returns a match where the string DOES NOT contain any word characters
    \Z Returns a match if the specified characters are at the end of the string

"""


"""

    findall: It finds all search for matches and print resultant in the form of a list.

    search: It works the same as a findall, but the resultant is a matched object, if any found.

    split: The split function splits the string from every matched into two new strings.

    sub: The sub-function works exactly like a replace function in notepad or MS Word, it replaces the original word, with a word of our choice.

    finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes than any other function defined above. It also provides more details related to the matched object. So, most of the examples we are going to see next will contain a finditer function in them.

"""


"""

    \A:         the resultant is a match if the input characters are at the beginning of the string                
    \b          the resultant is a match whether the input characters are at the beginning or the end of a word                               
    \d          the resultant is a match if the string contains any digits  
    \s           the resultant is a match if the string contains a white space character

"""

"""
There are many metacharacters supported by the re module. Some characters with their working are the following:

    '.': Matches any single character except newline
    '$': Anchors a match at the end of a string
    ' *': Matches zero or more repetitions
    '+':Matches one or more repetitions
    '{}':Matches an explicitly specified number of repetitions
    '[]':Specifies a character class

"""

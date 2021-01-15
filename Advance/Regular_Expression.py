import re

x='''1[Late Latin programma, from Greek] : a public notice
2a: a brief usually printed outline of the order to be followed, of the features to be presented, and the persons participating (as in a public performance)
b: the performance of a program
especially : a performance broadcast on radio or television
3: a plan or system under which action may be taken toward a goal
4: CURRICULUM
5: PROSPECTUS, SYLLABUS   inin
1910510-3033
programmed or programed; inn programming or programing'''


# Meta charactors -->

 a=re.compile(r"programming")     # WE want to search programming in x (string)
 b=a.finditer(x)
 for i in b:
     print(i)
     print(x[432:443])           # This will print span

# Using Meta charactors -->

 a=re.compile(r".program")     # WE want to search words which contains word program in x (string)
 b=a.finditer(x)
 for i in b:
     print(i)

# Starts with and Ends with -->

 a=re.compile(r"^program")     # It checks if x starts with program --> OP --> kuch nahi aaiye ga
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r"programing$")     # It checks if x ends with programing
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r"in*")     # one I and n can occur any times (n can be zero)
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r'in+')     # one I and atleast one n
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r'in{2}')     # one I only 2 times n
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r'(in){2}')     # It creates group --> inin occurs or not
 b=a.finditer(x)
 for i in b:
     print(i)

# Either or

 a=re.compile(r'in{2} | in')     # Either inin or in
 b=a.finditer(x)
 for i in b:
     print(i)


## Special Sequences -->

 a=re.compile(r'\A radio')     # Starts with radio or not
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r'\b radio')     #  word starts with radio or not
 b=a.finditer(x)
 for i in b:
     print(i)

 a=re.compile(r' radio \b')     #  word ends with radio or not
 b=a.finditer(x)
 for i in b:
     print(i)

a=re.compile(r'\d{7}-\d{4}')     # number --> 1910510-3033 --> seven digit - four digit
b=a.finditer(x)
for i in b:
    print(i)
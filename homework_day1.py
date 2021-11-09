# homework 1
# first example
# if __name__ == '__main__':

    #  places = [' ', 'Argentina', '  ', 'San Diego',
#           '', '   ', '', 'Boston', 'New York']
    
#     places = ' '.join(places).split()
# print(places)


# = [Argentina, San Diego, Boston, New York]

# # HINT: LOOK FOR A STRING METHOD THAT REMOVES WHITESPACE

# def vacation(self):
#     places = [' ', 'Argentina', '  ', 'San Diego',
#                 '', '   ', '', 'Boston', 'New York'].strip()
        



#     filter_object = filter(lambda x: x != '', places)

#     without_empty_strings = list(filter_object)

    
  
#     print(without_empty_strings)
#     print(places)


# Homework 2
# .sort(key=)

# HINT: YOU'LL NEED TO CONVERT EACH PERSON'S NAME (A STRING) INTO A LIST IN ORDER TO GRAB THE LAST NAME BY
# THE INDEX
# REAL WORLD EXAMPLE
# authors = ["Connor Milliken", "Victor aNisimov",
#            "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

# author_last_names = []
# for name in authors:
#   author_last_names.append(name.split()[-1])

# print(author_last_names)


# hw.3



# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32




# def Celsius(T):  
#     return T - 32 * (5/9)
    
# places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]




# list(map(Celsius, places ))



# hw4

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = 20

for f in range(nterms):
    print(fibo(f))

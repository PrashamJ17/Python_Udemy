from random import *

# print(random.random()) # gives a floating point no. btwn 0 and 1


# print(randrange(10)) # gives a random +ve integer value till 10
# print(randrange(20,100,2)) # gives a random +ve integer value btwn 20 to 100 with a step size of 2

# print(randint(-100,99)) # gives a random integer value bywn 1 and 99
# Alias for randrange(a, b+1) except it can take -ve values as well

# print(getrandbits(2)) # gives an integer with no. of bits = 2

# print(bin(7)) # converts the no. to binary

alphabets = ['ap','hi',2,'',[],[1,'alv',['a',33]]]
# print(choice(alphabets)) # gives a random element from the list

list_1 = choices(alphabets,k=3) # gives a list of total elements 3 fromm alphabet list, with replacement i,e they can be repeated 
print(list_1)

shuffle(list_1) # suffles the positon of te elemets in the list

sample(alphabets,5) # gives a 5 elemnt list from alphabets the elements wont be repeated 
#  similar to choices just the lements wont be repeated 

random() # gives a random floarting point no. btwn 0 and 1
uniform(1,10) # gives a random floating point no. btwn 1 and 10





























# # random.seed(a)
# for a in range(100):
#     random.seed(a)
#     num = random.randint(1,10)
#     if num==2 :
#         print(f"Seed for 2 : {a}")
#         break

# random.seed(14)
# print(random.randint(1,10))

# # random.seed(a) --> where a can be a string,integer,float or bytes form . 
# # it converts other things to integer and for that value of a whatever the next fn 
# # for eg random.randint() , it will give the same no. for that value of a

# # random.getstate()

# random.getstate()
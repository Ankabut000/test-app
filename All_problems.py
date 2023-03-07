# arr = []
# for i in range(3):
#     arr.append(input())
# new = [
#         [],[arr[0]],[arr[1]],[arr[2]],
#         [arr[0],arr[1]], [arr[1],arr[2]],
#         [arr[0],arr[2]],[arr[0],arr[1],arr[2]]
#       ]
# print(new)

##############################################################

# scrabble = list(input())
# ball = 0
# for i in scrabble:
#     if i.lower() in 'aeiounstr':
#         ball+=1
#     elif i.lower() in 'dg':
#         ball+=2
#     elif i.lower() in 'bcmp':
#         ball+=3
#     elif i.lower() in 'fhwvy':
#         ball+=4
#     elif i.lower() in 'k':
#         ball+=5
#     elif i.lower() in 'jx':
#         ball+=8
#     elif i.lower() in 'qz':
#         ball+=10
# print(ball)

################################################################

# arr = list(input())
# new = []
# for i in arr:
#     if new.count(i) != 0:
#         print(f"{i}_{new.count(i)}",end=' ')
#         new.append(i)
#     else:
#         print(f"{i}",end= ' ')
#         new.append(i)

################################################################


# def sanoq(str:str):
#     lst = str.split('.')
#     return int(lst[0]) * 256**3 + int(lst[1]) * 256**2 + int(lst[2]) * 256**1 + int(lst[3])* 256**0

# dct = {}
# n  = int(input())

# for i in range(n):
#     a = input()
#     dct.update({sanoq(a):a})
# new = list(dct)
# new.sort()
# for i in new:print(dct[i])


#################################################################

# '''
# Hello, world! Python IS programming language of thE future.My EMAIL is....
# Python is awesome!!!!
# '''


# sozlar = ['hello' ,'email' ,'python', 'exam' ,'the' , 'wor', 'is']

# gap = "Hello, world! Python IS programming language of thE future.My EMAIL is....\n\
# Python is awesome!!!!"


# gap = input("Gap kiriting: ").lower()

# f = open("forbidden_words.txt",'r')
# a = []
# for i in f.read().split():
#     a.append(i)

# for i in a:
#     if i in gap:
#         gap = gap.replace(i, len(i)*"*")

# print(gap)
























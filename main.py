# sample 1
# a=50
# b=50
# if b>a:
#     print("hello")
# elif b==a:
#     print("same value")
# else:
#     print("hi")

# sample 2
# i=11
# while i<10:
#     print(i)
#     i+=5

# sample 3
# a=["mubi","sana","hiba","sahala"]
# x=input("enter a name:")
# for x in a:
#     print(x)

# sample 4
# sum=0
# for i in range(1,21):
#     sum=sum+i
# print(sum)

# sample 5
# x=int(input("enter a number:"))
# sum=0
# for i in range(1,x+1):
#     sum=sum+i
# print(sum)

# even numbers
# for i in range(2,51,2):
#     print(i)

# odd and even numbers
# for i in range(1,11):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print(i,"is odd ")


# multiplication table
# x=int(input("enter a number"))
# for i in range(1,11):
#     mul=x*i
#     print(x,"X",i,"=",mul)


# adding names to list
# list1=[]
# for i in range(1,6):
#     x=input("enter a name:")
#     list1.append(x)
# print(list1)


# adding odd and even numbers to list
# odd=[]
# even=[]
# for i in range(1,11):
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)


# count odd numbers
# count=0
# for i in range(21,41,3):
#     count=count+1
# print(count)


# sample
# list=[]
# list2=[]
# for i in range(12,100,12):
#     list.append(i)
# print(list)
# for i in list:
#     if i%14==0:
#         list2.append(i)
# print(list2)

# check whether a number is prime or not
# num=int(input("enter a number:"))
# if num>1:
#     for i in range(2,num):
#         if (num%i) == 0:
#             print(num,"not a prime number")
#             break
#     else:
#         print(num, "is a prime member")
# else:
#     print((num,"is not a prime number"))

# to print all prime numbers upto n
n=int(input("enter a limit"))
for num in range(1,n):
    if num==1:
        print(num,"is not a prime number")
    else:
        for i in range(2,num):
            if (num%i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

















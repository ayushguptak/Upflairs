                #Question 1
n = int(input("Enter A Number : "))
if n < 0:
    print("Enter A Valid Number")
elif n == 0:
    print(1)
else:
    fact = 1
    while( n > 0 ):
        fact  = fact * n
        n = n-1
print(fact)


            #Question 2
import os
file = open( "demo.text", "w" )
file.write( "With Great Power Comes Great Responsibility\n" )
file.write( "Hope is a good thing, maybe the best of things\n" )
file.write( "I AM IRON MAN\n" )
file.write( "I'm the king of the world!\n" )
file.write( "babumoshai zindagi badi honi chahiye lambi nhi\n" )
file1 = open("demo.text" , "r")
for line in file1 :
    words = line.split()
    word_count = len(words)
    print(f" {line} -> word count : {word_count} \n " )
    
file1.close()


            #Question 3
list = [4,21,5,7,3,10,20,12,17]
max = list[0]
min = list[0]
for i in list:
    if i > max:
        max = i
    if i < min :
        min = i
print(f"{max} is the maximum element")
print(f"{min} is the minimum element")


            #Question 4
list = [ "INDIA" , "ARGENTINA", "AFRICA" , "CHINA" , "AUSTRALIA" , "ARIZONA" , "AMERICA" ]
max = list[0]
for i in list :
    if len(i) > len(max):
        max = i
        larget_word = max

print(larget_word)
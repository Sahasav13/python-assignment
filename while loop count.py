#Write a program using a while loop to count the number of digits in a given number

num = int(input("enter the number :"))
count =0

while num>1:
    num = num/10
    count +=1

print(f"the number of digits in the given number : {count}")

              

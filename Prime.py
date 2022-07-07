Test = 100
j = 1

a = []

while (j <= 100):
    num = j
    i = 1
    counter = 0
    while (i <= num):

        if (num % i) == 0:
            counter = counter+1
        i = i+1

# print(counter)
    if(counter == 2):
        print(f"{num} is a prime Number")
        a.append(num)

    # else:
       # print(f"{num} is Not a Prime number")
    j = j+1

print(len(a))

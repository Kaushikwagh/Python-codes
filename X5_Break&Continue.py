# Break and countinue 
    #Break:- Used to terminate the loop when encountered
    #Continue:- Terminates execution in the current iteration & countinues execution of the loop with the next iteration.

i = 1
while i<=5:
    print(i)
    if(i == 3):
        break       # break
    i += 1

print("end")
print()
# - - - - - - - - - - -

i =0
while i <=5:
    if(i == 3):
        i += 1
        continue    # 3 Skip
    print(i)
    i+=1

print("end")

# - - - - - - - - - - -

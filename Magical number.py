import random
while True:
    rand_num = random.randint(0,10)
    inp_num = input("Enter a number from 0 to 10: ")
    try:
        if int(inp_num) in range(0,11):
            if rand_num == int(inp_num):
                print ("You've won. Congratulations!!")
                break
            else:
                print ("Uh..ho. Please try the game again")
                continue
        else:
            print ("Number is out of range..")
    except:
        print("Invalid input! Try again...")
        continue

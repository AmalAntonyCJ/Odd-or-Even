import random


Computer = random.randint(1,6)

Sum = None

PlayerToss = input ("choose Odd:(o) or Even:(e):\n") .lower()

TossNum = int( input ( "Choose Number for Toss :-" )  )

if (TossNum > 7 or TossNum < 1):
    print("Invalid Input \n Please Try Again")

else:
    print(f"You choose {TossNum} \n and Computer Choose {Computer}")
    SumToss =TossNum + Computer
    
    if (SumToss%2) == 0:
        Sum = "e"
        print("It's even")
        print("Choose For Even")
    
    else:
        Sum = "o"   
        print("It's odd")
        print("Choose for Odd")

if Sum == PlayerToss:

    BatorBowl = input("You have WON the Toss,Now You Can Choose to Bat(a) or Bowl(b) : ")

    if BatorBowl == "b":
       Balls = 100
       BallsBat = 0        
       PlayerRuns = 0
       print("--------------\nYour Batting\n")

       while BallsBat < Balls:
            Runs = int(input("Enter a Number to Bat: "))
            CompBowl = random.randint(1,6)
            
            if Runs == CompBowl:
                print (f"Your number is {Runs}, Computer's number is {CompBowl}")
                print (f"YOU ARE OUT \n Your Total Score is {PlayerRuns}\n")
                break

            elif Runs>7:
                print ("PLEASE TRY INPUTTING A NUMBER BELOW 6")
                continue

            else:
                PlayerRuns += Runs
                print (f"Your Number: {Runs}, Computer Number: {CompBowl}")
                print (f"Your Runs now are {PlayerRuns}\n")
            
            BallsBat += 1

       print ("-----------------------------------\nComputer batting\n")
       Balls2 = 100
       BallsBat2 = 0
       CompRuns2 = 0
       while BallsBat2 < Balls2:
             Bowl2 = int (input("Enter Runs to Bowl: "))
             CompBat2 = random.randint(1,6)
            
             if CompBat2 == Bowl2:
                print (f"Computer's number is {CompBat2}, Your Number is {Bowl2}")
                print (f"COMPUTER IS OUT. Computer's Total Runs are {CompRuns2}")
                break
             
             else:
                CompRuns2 += CompBat2
                print (f"Computer's number is {CompBat2}, Your number is {Bowl2}")
                print (f"Computer's score is {CompRuns2}\n")
                
                if CompRuns2 > PlayerRuns:
                    break
             BallsBat2 += 1

    print("-----------------------------------\nRESULTS: ")
            
    if CompRuns2 < PlayerRuns:
             print (f"\nYou have WON THE GAME. \n\nYour Total Runs are {PlayerRuns} in {BallsBat} Balls  Computer Scored {CompRuns2} in {BallsBat2} Bowls")
    elif CompRuns2 == PlayerRuns:
             print (f"The GAME IS TIE, You score {PlayerRuns} and the Computer also Scored {CompRuns2}")
    else: 
             print (f"\nComputer WON THE GAME \nComputer Total Runs are {CompRuns2} in {BallsBat2} Bowls \nYou Score {PlayerRuns}")
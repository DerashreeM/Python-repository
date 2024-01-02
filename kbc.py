'''This Game Developed by - Meet Mehta'''

print("Welcome to KBC!!!!!")
name=input("enter your name=>")
print("let's begains!",name)
print("Rules of the game \n 1.question is from 1 to 7 each contins various value \n 2.select answer from 4 option \n 3.Question no=3,5 is the rest level \n 3.question 7 is the jackpot level wroth of Rs.1cr")
print("\n so,question is on your laptop screen!!!!!")

questions=[

    ["who is the prime minister of india?","nitin gadkari","adani","ambani","modi",4],
    ["who is the home minister of india?","amit shah","modi","s jishankar","jay shah",1],
    ["who is the president of india?","nitin gadkari","adani","ambani","draupadi murmu",4],
    ["who is the caption of CSK?","mahi","raina","jadeja","kohali",1],
    ["who is the leader of Congress?","rahul gandhi","malikarjun khadke","sonia gandhi","ashok grhlot",2],
    ["how many players are there in kabaddi?","three","sevan","six","elevan",3],
    ["who is the current CJI of india?","ajit dobhal","s jaishankar","d y chandrachud","shaktikant das",3]

    ]
levels=[1000,25000,50000,125000,200000,500000,10000000]
money=0
for i in range(0,len(questions)):
    question =questions[i]
    print(f"\n*question for Rs.{levels[i]} is \n {question[0]}")
    print(f"1.{question[1]}     2.{question[2]}")
    print(f"3.{question[3]}     4.{question[4]}")
    replay=int(input("Enter your answer=>"))
    if(replay==question[-1]):
        print(f"\n Correct answer,you have won Rs.{levels[i]} congrats",name)
        print(f"let's move on to next question....")
        if(i==2):
            money=50000
        elif(i==4):
            money=200000
        elif(i==6):
            money=10000000
    else:
        print("ohhhh,wrong answer!!!!",name)
        break

print("Well played!!",name,"your final prize money is ",money)
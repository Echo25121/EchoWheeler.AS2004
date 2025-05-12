# Setting functions, lists and variables
Str_Answer = 0
Cor_answer = 0
Str_Continue = 0
Intro = 'Hello and welcome to my quiz!'
'This Quiz is about animals',
Int_score = 0
Game_Start = 1
Int_Num_Question = 0
Game_end = 0
count = 0


#Where I set Questions
questions = [
    ["What does Gandalf the Grey say to the Balrog to protection the fellowship", [
        ["(1) You shall not pass!"],
        ["(2) please stay there"],
        ["(3) Die foul beast!"],
        ["(4) I will kill you"]
    ], "1"],
    ["What is the first lotr movie created called?", [
        ["(1) Lord of the rings: Journey to mount doom"],
        ["(2) Lord of the rings: fellowship of the ring"],
        ["(3) Lord of the rings: return of the king"],
        ["(4) The hobbit"]
    ], "2"],
    ["Who helped Frodo the most", [
        ["(1) Saruman"],
        ["(2) Legolas"],
        ["(3) Dobby"],
        ["(4) Samwise Gamgee"]
    ], "4"], 
    ["What is the spider that Frodo and Samwise Gamgee run into called?", [
        ["(1) Gleeok"],
        ["(2) Helob"],
        ["(3) Ungoliath"],
        ["(4) Shelob"]
    ], "4"],
    ["Who dies at the end due to their love of the ring?", [
        ["(1) Gollum"],
        ["(2) Bilbo Baggins"],
        ["(3) Frodo"],
        ["(4) Dobby"]
    ], "1"]
]

# Function for Questions
def askQuestion(name, answers, Cor_answer,Int_score):
    
    print(name)
 
    for answer in answers:
        print(answer[0])
        #print(answer[1])
    Str_Answer = input("")

    if Str_Answer == Cor_answer:
        print('Correct! :D')
        Int_score = Int_score +1
    
    else: 
        print("Incorrect :(")
       
    Str_Answer = 0

    print ('The Answer is ' + Cor_answer)
   
    return Int_score
#Game running
while Game_Start == 1:
    Game_Start = 0
    print(Intro)
    print('You will have to answer one out of four different choices 1, 2, 3 or 4')
    print()
    for question in questions:
        Int_score = askQuestion(question[0], question[1], question[2], Int_score)
    print ("Your score is " + str(Int_score))
    if Int_score == 5:
        print('Congratulations you got all of them right!')
    print("Do you want to try again? Y/N") 
    Int_score = 0
    #Game Ending
    Game_end = 1
    while Game_end == 1:
        Game_end = 0
        Str_Continue = input("")
        if Str_Continue == "Y" or Str_Continue == "y":
            Game_Start = 1
        elif Str_Continue == "N" or Str_Continue == "n":
            print("Good bye")
            quit()
        else:
            print("Please choose Y or N")
            Game_end = 1
            count += 1


        
        
        
        
        
        

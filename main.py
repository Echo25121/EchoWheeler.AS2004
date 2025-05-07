# Setting functions, lists and variables
Str_Answer = 0
Cor_answer = 0
Str_Continue = 0
Intro = 'Hello and welcome to my quiz!'
'This Quiz is about animals',
Int_score = 0
Game_Start = 1
Int_Num_Question = 0

#Where I set Questions
questions = [
    ["What mammal doesn't lay eggs", [
        ["(1) Horse"],
        ["(2) Long Beaked Echidna"],
        ["(3) Short Beaked Echidna"],
        ["(4) Platypus"]
    ], "1"],
    ["Which animal was recently claimed by scientests to have had a de-extinction", [
        ["(1) Wooly Mammoth"],
        ["(2) Dire Wolf"],
        ["(3) Velociraptor"],
        ["(4) Tuatara"]
    ], "2"],
    ["What modern day animal has the strongest biteforce", [
        ["(1) Fantail"],
        ["(2) Tyrannosuarus rex"],
        ["(3) Golden retriever"],
        ["(4) Saltwater Crocodile"]
    ], "4"]
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

while Game_Start == 1:
    Game_Start = 0
    print(Intro)
    print('You will have to answer one out of four different choices 1, 2, 3 or 4')
    print()
    for question in questions:
        Int_score = askQuestion(question[0], question[1], question[2], Int_score)
    print ("Your score is " + str(Int_score))
    if Int_score == 3:
        print('Congratulations you got all of them right!')
    print("Do you want to try again? Y/N") 
    Int_score = 0
    Str_Continue = input("")
    if Str_Continue == "Y" or Str_Continue == "y":
        Game_Start = 1
    elif Str_Continue == "N" or Str_Continue == "n":
        print("Good bye")
        quit()
    else:
        print("Please choose Y or N")
        
        
        
        
   
        

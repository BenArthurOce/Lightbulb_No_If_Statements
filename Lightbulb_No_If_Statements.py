


#DICTIONARY THAT HOLDS ALL THE QUESTIONS
#=======================================

def fResponse_To_Question(stage,resp):
    dict =  {

        #Is the Light on?  
        #If not, Go to Stage 2
        (1,"Qst")   : [1, 'Is the Light on?'],
        (1,"Yes")   : [9, 'Good, All is Okay'],
        (1,"No")    : [2, ''],

        #Is the electricity turned off?
        #If not, Go to Stage 3
        (2,"Qst")   : [2, 'Is the electricity turned off?'],
        (2,"Yes")   : [9, 'Turn on Electricty at the Switch'],
        (2,"No")    : [3, ''],

        #Has the light globe blown?
        #If not, Go to Stage 4
        (3,"Qst")   : [3, 'Has the light globe blown?'],
        (3,"Yes")   : [9, 'Replace the Light Globe'],
        (3,"No")    : [4, ''],

        #Has the fuse blown?
        #If Yes, Replace the Fuse
        #If No,  Call an Electrician
        (4,"Qst")   : [4, 'Has the fuse blown?'],
        (4,"Yes")   : [9, 'Replace the Fuse'],
        (4,"No")    : [9, 'Call an Electrician'],
        }

    Dictionary_Result = dict[stage, resp]
    return Dictionary_Result



#Produce String Line that gives the user a question for input
#=======================================

#"a" is the stage/question number we are at (1 to 4) - KEY 1
#"Qst" is automatic in order to lock in the question key - KEY 2
def fAsk_Question(a,b="Qst"):
    question = fResponse_To_Question(a,"Qst")[1] + "  "
    return question



#Main Looping Code
#=======================================
iStage = 1      #"iStage" is the question number to be asked. There are 4 questions
while iStage != 9:

    #Prompt User with Input, Generated from Dictionary Function
    #Key 1 is the current stage, Key 2 is "Qst/Yes/No". ("Yes/No" based on player input)

    question = fAsk_Question(iStage)            #Question for Input Line
    response = input(question).title()          #Can be a "Yes" or "No"


    #Set a response to be printed later. This will change based on how often looped
    #Set the stage number to the next question (+1 if next question, or set to 9 to end the loop)

    sResp = fResponse_To_Question(iStage,response)[1]   #Changing response stored for end result
    iStage = fResponse_To_Question(iStage,response)[0]  #Next Question to be asked (9 exits)



#Give End Result and End Code
#=======================================
print(" ")
print(sResp)

print(" ") 
print("===================================")
print("Thank you for using troubleshooter.")
print("===================================")
print(" ") 
#This script lets the user generate made-up participants with partipant number, gender, whether they have taken drugs and RT (reaction times)
#This script is useful if you want to play around with statistics

#Here we have all the prereqs.
import random #the random module is imported. We need it later, when we ask Python to pick random genders and reaction times

#These are the lists that the participant generator can select from
ListOfGenders = ["male","female"] #here are the genders that Python can pick from in a list
TakenDrugs = ["Yes","No"]#here are the choices the participants have for whether they have taken drugs or not 

#Here we have the participant genertator
def ParticipantGenerator():
    ParticipantFile = open('ParticipantData.txt','w')#opens a file called participantdata 
    for x in range(int(NumberOfParticipants)): #Repeats the given process x times where x is the number of participants input.
        ParticipantNumber = 1 #This gives us the participant number
        ParticipantNumber = ParticipantNumber + x #now the number increases for each participant generated 
        ParticipantGender = random.choice(ListOfGenders) #Python selects a gender for the first participant
        ParticipantDrugs = random.choice(TakenDrugs)
        ParticipantRT = random.randint(100,600) #we get a random reaction time
        ParticipantFile.write(str(ParticipantGender) + "," + str(ParticipantDrugs) + "," + str(ParticipantRT) + ",")#we append our text document with each participant that we want generated 
        #variable to keep track of a certain mean ½

#THE INSTRUCTIONS TO GET THE SCRIPT RUNNING
while True: #start out by 
    try:
        StopScript = input("Please write stop now to stop the script, otherwise input anything else ")#instructions if you want to stop
        if StopScript == "stop":
                break 
        NumberOfParticipants = int(input("Please indicate how many Participants you want to generate. This overwrite any previous participants "))#Here the researcher can put in how many participants he/she wants to generate - and the script does it as many times as you want
        ParticipantGenerator() #start the function if a whole number is input
    except ValueError: #what will happen, if a whole number is NOT input
           print("Sorry, please enter a whole number")
           continue #go back to the beginning of the function if an integer is not input as the number of participants 

#generate significant differences in a certain % of the cases
#calc SD for a randomised dataset - should be able to generate a dataset with a certain Mean, SD 


#save a tab separated file -text file/exceltab/commmaseparated      
#ParticipantFile = open('ParticipantData','w')
#ParticipantFile.write(#the participants that were generated)
#ParticipantFile.close()



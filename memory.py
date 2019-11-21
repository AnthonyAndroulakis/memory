#this file represents the (new) structure of memory

import numpy as np #for time and space (boolean) matricies. 1 for occurs and 0 for not occurs.
#needs to account for time and space (location)

time=2 #2 seconds, or whatever unit of time. Either this time unit changes, the weight for each experience in a time slot, or both
width=3 #unit space 1 dimensional, this changes
height=4 #unit space 1 dimensional, this changes
currentspace= np.zeros((time, width, height)) #initialize 3x4 unit2 space with 2 seconds of time
#3d currentspace is a stream of spacial-temporal experiences, only time and location covered in this matrix
current={} #current contains a non-rigid area of space made up of current space variables over time. keys=time, values=(currentspace variables)

#####START BIASES##### 1 (equal bias/weight) for now
newBias=1
newWeightStartHabit=1
newWeightNeeded=1
newWeightPast=1
newWeightPredict=1
#####END BIASES#####

import linecache #to simulate outside and inside perception stream, inside perception stream created from outside (whatever has been "normalized")
import os #to simulate random noise

class MemoryException(Exception):
    pass

where=[]
locations=[]
nowLoop=[]

#build variables
newlocation=input("present location: ") #change
oldlocation=input("past location: ") #change
where.append(newlocation) #location for "present"
locations.append(oldlocation) #location for "automaticHabits"

#automaticHabits
startHabits = dict.fromkeys(locations) #starting actions for habits
needed = dict.fromkeys(locations) #needed for survival
past = dict.fromkeys(locations) #past memories, long term memories, if multiple memories in specific location add as list
predict = dict.fromkeys(locations) #predictions/biases about the future. Note, predictions/biases about the past are counted as self-feedback-loop (part of perception stream)

##if len(locations) != len(list(startHabits.keys())) + len(list(needed.keys())) + len(list(past.keys())) + len(list(predict.keys())): #if at anytime the # of automaticHabits exceeds the # of specifit locations, put up an error. This is to prevent over-self-feedbacking.
##     raise MemoryException("Automatic Habit Memory leak.")

i=0 #remove this line

k=0 #remove this line
k1=k #remove this line
k2=k #remove this line
k3=k #remove this line
k4=k #remove this line

nowLoop.append(newBias) #individual loop to account for constantly feedback loop, add random noise
startHabits[locations[k1]]=newWeightStartHabit #k instead of i to describe anything other than present
needed[locations[k2]]=newWeightNeeded
past[locations[k3]]=newWeightPast
predict[locations[k4]]=newWeightPredict

if len(nowLoop) != len(where): #if at anytime the # of working memories is different from the # of locations, put up an error. This is to prevent over-self-feedbacking.
     raise MemoryException("Working memory leak.")

memory = {"present": {','.join(where): nowLoop}, "automaticHabits": {','.join(locations): {"startHabits,needed,past,predict": [startHabits, needed, past, predict]}}} #variables constantly changing, structure stays the same
print(memory)

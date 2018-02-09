import pandas as pd
import numpy as np
import datetime
from todoist.api import TodoistAPI
import pytz

myToken = '6de0c48443150c63ac197ac8fb141a00e471eb03'
api = TodoistAPI(myToken)

def my_range(start, end, step):
    while start < end:
        yield start
        start += step

# Project_Id, Project_Name, Item_Id, Item_Name, Completed_Date, Label
mylim = 50

projectId, projectName, itemId, itemName, completedDate, label = [], [], [], [], [], []

for myoffset in range(0,1400,50):
    #print ('MyOffset is the following: ' + str(myoffset))

    qaqa = api.completed.get_all(limit = mylim, offset = myoffset, until = '2017-12-31T23:13', since = '2017-1-1T00:01')
    myRng = int(len(qaqa['items']))

    for z in my_range(0,myRng,1):
        #print ('The value z is the following: ' + str(z))
        #print (qaqa['items'][z]['content'])
        projectId.append(qaqa['items'][z]['project_id'])
        itemId.append(qaqa['items'][z]['id'])
        itemName.append(qaqa['items'][z]['content'])
        completedDate.append(qaqa['items'][z]['completed_date'])

print (len(projectId))

import pandas as pd
import numpy as np
import datetime
from todoist.api import TodoistAPI

myToken = '6de0c48443150c63ac197ac8fb141a00e471eb03'
api = TodoistAPI(myToken)
api.sync()

# print(api.state['projects'][1:3])

##### Function List #####

def my_range(start, end, step):
    """Custom loop counter.
    Args:
        start: Initial value.
        end: Terminal value.
        step: Increment value.

    Returns:
        start: List of loop values.
    """
    while start < end:
        yield start
        start += step

##### Create Item Table #####

endDate = '2018-01-01T05:00'
startDate = '2017-01-01T05:00'

#endDateFmt = datetime.datetime.strptime(endDate, "%Y-%m-%dT%H:%M")
countDateFmt = datetime.datetime.strptime(endDate, "%Y-%m-%dT%H:%M")
startDateFmt = datetime.datetime.strptime(startDate, "%Y-%m-%dT%H:%M")

bufferSize = 50
bufferStart = 0

projectId, projectName, itemId, itemName, completedDate, label = [], [], [], [], [], []

# for bufferStart in range(0,1500,50):
while (countDateFmt > startDateFmt):

    itemBuffer = api.completed.get_all(limit=bufferSize, offset=bufferStart, until=endDate, since=startDate)
    # print(int(len(itemBuffer['items'])))
    bufferLength = int(len(itemBuffer['items']))

    for bufferIndex in my_range(0, bufferLength, 1):
        projectId.append(itemBuffer['items'][bufferIndex]['project_id'])
        itemId.append(itemBuffer['items'][bufferIndex]['id'])
        itemName.append(itemBuffer['items'][bufferIndex]['content'])
        completedDate.append(itemBuffer['items'][bufferIndex]['completed_date'])

    bufferStart += bufferLength
    countDateFmt = countDateFmt - datetime.timedelta(days=7)


itemTable = pd.DataFrame({'Project_Id' : projectId,
                          'Project' : None,
                          'Item_Id' : itemId,
                          'Content' : itemName,
                          'Date' : completedDate,
                          'Energy' : None,
                          'Time' : None})

itemTable = itemTable[['Project_Id', 'Project', 'Item_Id','Content', 'Date', 'Energy', 'Time']]

# print(itemTable.head(10))
# print(itemTable.shape)
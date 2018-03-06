import pandas as pd
from todoist.api import TodoistAPI

myToken = 'PLACE TOKEN HERE'
api = TodoistAPI(myToken)
api.sync()
# print(api.state['projects'][1:3])

##### Function List #####

def parseProjectData(sourceProjectData, idList, projectList, colorList, parentIdList):
    """Creates subset of relevant project data from raw API output.
    Args:
        sourceProjectData: Dictionary of project data pulled directly from ToDoist API.
        idList: List containing project id(s).
        projectList: List containing project names.
        colorList: List containing project colors.
        parentIdList: List containing parent id(s).

    Returns:
        idList: List containing project id(s).
        projectList: List containing project names.
        colorList: List containing project colors.
        parentIdList: List containing parent id(s).
    """

    for sourceProject in sourceProjectData:
        myId.append(sourceProject['id'])
        myProjects.append(sourceProject['name'])
        myColor.append(sourceProject['color'])
        myParentId.append(sourceProject['parent_id'])

    return idList, projectList, colorList, parentIdList

##### Create Project Table #####

# currentProjectData = api.state['projects']
currentProjectData = api.state['projects']
archivedProjectData = api.projects.get_archived()

myId, myProjects, myColor, myParentId = [], [], [], []
myId, myProjects, myColor, myParentId = parseProjectData(currentProjectData, myId, myProjects, myColor, myParentId)

projectTable = pd.DataFrame({'id' : myId,
                             'parent_id' : myParentId,
                             'color' : myColor }, index = myProjects, dtype = 'int64')

projectTable = projectTable[['id','color','parent_id']]
projectTable.fillna('None', inplace=True)

projectTable.to_csv('projectTable.csv')
# print (projectTable)

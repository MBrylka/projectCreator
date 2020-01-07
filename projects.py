import os
import sys
from configparser import ConfigParser
from pathlib import Path

config = ConfigParser()
config.read(os.path.dirname(os.path.realpath(sys.argv[0]))+'/config.ini')
root = config.get('github', 'PROJECTS_FOLDER')#"C:/Users/macie/Documents/Projects/"


if len(sys.argv) > 1:
    option = sys.argv[1]
    if option == 'show':
        print('Projects:\n-----------------')
        projectsDict = os.listdir(root)
        for pdir in projectsDict:
            print(pdir)
        print('')

    elif option == 'open':
        if len(sys.argv) > 2:
            if os.path.exists(root+'\\'+sys.argv[2]):
                os.system('code '+root+'\\'+sys.argv[2])
            else:
                print(root+'\\'+sys.argv[2])
                print('no project with that name')
        else:
            print('project name was not specified')

    elif option == 'info':
        if len(sys.argv) > 2:
            if os.path.exists(root+'\\'+sys.argv[2]):
                os.system('powershell cat '+root+'\\'+sys.argv[2]+'/README.md')
            else:
                print('no project with that name')
        else:
            print('project name was not specified')
    elif option == 'create':
        if len(sys.argv) > 2:
            os.system('python '+str(Path('projects.exe').resolve())+'/createProj.py -p '+sys.argv[2])
        else:
            print('project name was not specified')
    else:
        print('please use command: \nproject show|open|create')
else:
    print('please use command: \nproject show|open|create')

import argparse
import os
import subprocess
from configparser import ConfigParser
import io

from github import Github

if __name__ == '__main__':
    
    config = ConfigParser()
    config.read('config.ini')

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--project')
    parser.add_argument('-i', '--info')
    args = parser.parse_args()
    
    if(args.project):
        project_path = os.path.join(config.get('github', 'PROJECTS_FOLDER'), args.project)
        project_exists = os.path.isdir(project_path)
        if not project_exists:
            os.mkdir(project_path)
            g = Github(config.get('github', 'GIT_TOKEN'))
            user = g.get_user()
            repo = user.create_repo(args.project)
            print(repo)

            os.chdir(project_path)
            os.system(F'"#New repository of {args.project}" >> README.MD')
            os.system('git init')
            os.system(F'git remote add origin https://github.com/MBrylka/{args.project}')
            os.system('git add *')
            os.system('git commit -m "First commit"')
            os.system('git push origin master')
            os.system('code .')
            print(args.project, 'created')
        else:
            print('project with that name already exists')
    else:
        print('makeproj -p nameOfProject | --project nameOfProject')


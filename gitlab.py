import argparse
import fnmatch
import os
import webbrowser

PROJECT_DIR = 'C:/Users/ryan.wong/Projects/'
BACKEND_GITLAB_URL = 'http://www.google.com'

parser = argparse.ArgumentParser(description='Open a file on GitLab by inputing the project name and filename')
parser.add_argument('-p', '--project', help='name of the project')
parser.add_argument('-f', '--file', help='name of the file')

args = parser.parse_args()

project_name = args.project
file_name = args.file

matches = []
for root, dirnames, filenames in os.walk(PROJECT_DIR + project_name):
    for filename in fnmatch.filter(filenames, file_name):
        matches.append(os.path.join(root, filename))

if (matches.length == 0):
	print 'No class %s was found within project %s' % file_name, project_name
elif (matches.length > 1):
	print 'More than 1 file named %s has been found within project %s' % file_name, project_name
else:
	webbrowser.open_new_tab(BACKEND_GITLAB_URL + matches[0])	
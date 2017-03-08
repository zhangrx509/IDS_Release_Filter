#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import sys
import subprocess
import re

if len(sys.argv) != 4:
    print('''Usage:
    release_filter.py <repo_root_path> <this_release_SHA-1> <last_release_SHA-1>''')
else:
    #change dir to git repo
    old_dir = os.getcwd()
    os.chdir(sys.argv[1])

    #output log contains JIRA project issues
    JIRA_project_key = 'IDSM'
    p = subprocess.run('git log --grep=' + JIRA_project_key + '- --pretty="%B"', stdout=subprocess.PIPE)  
    print(p.stdout.decode('ascii'))
    issue_log = p.stdout.decode('ascii') 

    #Get JIRA issue list
    list = re.findall(JIRA_project_key + r'-\d+',issue_log)
    print(list)

    #format release filter
    release_filter = 'Issuekey = ' + list[0]
    for issue in list[1:]:
        release_filter += ' OR Issuekey = ' + issue

    #output to release_filter.txt
    os.chdir(old_dir)
    output_file = open('release_filter.txt', 'w')
    output_file.write(release_filter)
    print('Done. Please see output in release_filter.txt')

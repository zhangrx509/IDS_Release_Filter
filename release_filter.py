
# get JIRA project key
JIRA_project_key = 'IDSM'
temp_key = input('Set JIRA project key, press ENTER to use default(' + JIRA_project_key + '):')
if temp_key != '':
    JIRA_project_key = temp_key
print('JIRA project key is set to ' + JIRA_project_key +'\n')

# get input for issue list
list = []
end = False
while not end:
    issues = input('Add JIRA Issue(s), press ENTER only to finish:')
    if issues == '':
        end = True
    else:
        list += issues.split()

        # print current issues to screen
        current_issues = ''
        for index, issue in enumerate(list):
            current_issues += JIRA_project_key + '-' + issue + ' ' 
            # change to new line every 4 issues
            if index % 4 == 3:
                current_issues += '\n                '
        print('Current issues: ' + current_issues)

#format release filter
release_filter = 'Issue key = ' + JIRA_project_key + '-' + list[0]
for issue in list[1:]:
    release_filter += ' AND Issue key = '  + JIRA_project_key + '-' + issue

#output to release_filter.txt
output_file = open('release_filter.txt', 'w')
output_file.write(release_filter)
print('Done. Please see output in release_filter.txt')

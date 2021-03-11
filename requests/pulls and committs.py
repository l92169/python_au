import requests
import json

TASK_PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'ITERATOR']
GROUPS = ['1011', '1012', '1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Fixed', 'Moved']
TOKEN = 'ad8c207f02cfa9d73fab37d4d85a5c6e2fe0ab22'


def prepare_headers():
    return {'Authorization': 'token ' + TOKEN,
            'Content-Type': "application/json",
            'Accept': "application/vnd.github.v3+json"
            }


def check_prefixes(title):
    result = []
    TF = True
    title = title.split()
    prefixes = title[0].split('-')
    if len(prefixes) == 2:
        pull_prefix, group = prefixes[0], prefixes[1]
        if pull_prefix not in TASK_PREFIX:
            TF = False
            result.append('The prefix of your message must contain prefix in {}'.format(TASK_PREFIX))
        if group not in GROUPS:
            TF = False
            result.append('The group number of your message must contain group number in {}'.format(GROUPS))
        if title[1] not in ACTION or len(title) < 2:
            TF = False
            result.append('The action of your message must contain action in {}'.format(ACTION))
    else:
        result.append('You need to write "-" between prefix of your message and group number')
        TF = False
    return '/n'.join(result), TF


def prepare_body(pr, errors):
    return {'body': '{}'.format(errors),
            'path': requests.get(pr['url'] + '/files', headers = prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}


def send_pr_comment(pr, errors):
    r = requests.post(pr['url'] + '/comments', headers = prepare_headers(), json = prepare_body(pr, errors))


def get_all_user_pr(user_login, repos_name, pr_state):
    url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repos_name, pr_state)
    pulls = requests.get(url, headers=prepare_headers())
    print(pulls.status_code)
    return pulls


def get_all_pr_commits(pr):
    url = pr['commits_url']
    commits = requests.get(url, headers=prepare_headers())
    return commits


def verify_pr(pr):
    message = 'Your pull request {}/n'.format(pr['title'])
    t, TF = check_prefixes(pr['title'])[0], check_prefixes(pr['title'])[1]
    message += t
    message += '\n\n'
    for commit in get_all_pr_commits(pr).json():
        comm = commit['commit']
        message += 'Your commit: {}\n'.format(comm['message'])
        com, TF_com = check_prefixes(comm['message'])[0], check_prefixes(comm['message'])[1]
        TF = TF * TF_com
        message += com
        message += '\n'
    if not TF: 
        return send_pr_comment(pr, message)


def main():
    user = 'l92169'
    repos = 'python_au'
    state = 'open'
    for pr in (get_all_user_pr(user, repos, state)).json():
        verify_pr(pr)
main()

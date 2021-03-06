import requests
import json

PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER', 'ITERATOR', 'TRIANGLE']
GROUPS = ['1011', '1012', '1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Fixed', 'Moved']
TOKEN = ''


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
    pull_prefix, group = prefixes[0], prefixes[1]
    if pull_prefix not in PREFIXES:
        TF = False
        result.append('Pull Request prefix must contain prefix in {}'.format(PREFIXES))
    if group not in GROUPS:
        TF = False
        result.append('Pull Request title must contain group number in {}'.format(GROUPS))
    if title[1] not in ACTION or len(title) < 2:
        TF = False
        result.append('Pull Request action must contain action in {}'.format(ACTION))
    return '/n'.join(result), TF


def send_pr_comment(pr, errors):
    r = requests.post(pr['url'] + '/comments', headers=prepare_headers(), json={'body': '{}'.format(errors),
                                                                                'path':
                                                                                    requests.get(pr['url'] + '/files',
                                                                                                 headers=prepare_headers()).json()[
                                                                                        0]['filename'],
                                                                                'position': 1,
                                                                                'commit_id': pr['head']['sha']})
    print(r.status_code)
    print(r.json())


def get_all_user_pr(user_login, repos_name, pr_state):
    url = 'https://api.github.com/repos/{}/{}/pulls?state={}'.format(str(user_login), str(repos_name), str(pr_state))

    pulls = requests.get(url, headers=prepare_headers())
    return pulls


def get_all_pr_commits(pr):
    url = pr['commits_url']
    commits = requests.get(url, headers=prepare_headers())
    return commits


def main():
    user = 'l92169'
    repos = 'python_au'
    state = 'open'
    for pr in (get_all_user_pr(user, repos, state)).json():
        if not check_prefixes(pr['title'])[1]:
            print(pr['title'])
            send_pr_comment(pr, check_prefixes(pr['title'])[0])


main()


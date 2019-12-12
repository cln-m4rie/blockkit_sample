import requests

from envs import WEBHOOK_URL


def post(data: dict) -> requests.Response:
    res = requests.post(WEBHOOK_URL, json=data, headers={
                        'Content-Type': 'application/json'})
    return res


def fetch_repos():
    res = requests.get('https://api.github.com/users/cln-m4rie/repos')
    res.raise_for_status()
    return res.json()


def main():
    repos = fetch_repos()

    blocks = [
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': 'GitHub API',
            }
        },
        {
            'type': 'divider'
        },
    ]
    for repo in repos:
        blocks.append(
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f"*{repo['name']}*\n"
                    f"Language: {repo['language']}\n"
                    f"Star: {repo['stargazers_count']}\n"
                    f"Last updated {repo['updated_at']}\n"
                    f"{repo['description']}\n"
                    f"<{repo['html_url']}|View this repository on GitHub>"
                },
            },
        )
        blocks.append({
            'type': 'divider'
        })
    post({'blocks': blocks})


if __name__ == "__main__":
    main()

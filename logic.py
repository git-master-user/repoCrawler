from github import Github


def main(git_user: str , programing_language=None, min_num_of_stars=0):
    results = get_user_repos(git_user)
    # print(filter_user_repos(results, programing_language, min_num_of_stars ))
    return filter_user_repos(results, programing_language, min_num_of_stars)


def get_user_repos(git_user: str = 'x4nth055'):
    token = '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'
    g = Github(token)

    # get that user by username
    user = g.get_user(git_user)

    return user.get_repos()


last_update = []

def filter_user_repos(repos: any, language: str = None, min_num_of_stars: int = 0):
    global last_update
    repo_data_list = []
    for repo in repos:

        if language and repo.language != language:
            continue

        if repo.stargazers_count < min_num_of_stars:
            continue

        commits = repo.get_commits()
        if commits.totalCount:
            last_update = (commits[0].commit.committer.date)

        repo_tuple = (repo.full_name, repo.description, repo.language,
                      repo.open_issues_count, repo.get_pulls().totalCount, last_update)

        repo_data_list.append(repo_tuple)

    return repo_data_list


# main()

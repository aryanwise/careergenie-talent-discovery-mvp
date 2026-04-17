def score_user(user, repos):
    followers = user.get("followers", 0)
    repo_stars = sum(r.get("stargazers_count", 0) for r in repos)

    activity_score = len(repos) / 10
    popularity_score = followers / 100

    score = (
        activity_score * 0.4 +
        popularity_score * 0.3 +
        (repo_stars / 500) * 0.3
    )

    return round(score, 2)
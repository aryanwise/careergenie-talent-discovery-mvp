def infer_roles(repos):
    roles = set()

    for repo in repos:
        lang = repo.get("language", "")

        if lang in ["Python", "Go"]:
            roles.add("Backend Engineer")

        if lang in ["JavaScript", "TypeScript"]:
            roles.add("Frontend Engineer")

        topics = repo.get("topics") or []
        if "machine-learning" in topics:
            roles.add("ML Engineer")

    return list(roles)
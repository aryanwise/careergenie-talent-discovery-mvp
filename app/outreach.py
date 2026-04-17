def generate_message(user, roles):
    role = roles[0] if roles else "engineering"

    return f"""
Hi {user.get('login')},

I came across your GitHub profile and really liked your work.

We’re building something exciting at CareerGenie and think you'd be a great fit for a {role} role.

Would love to connect!

"""
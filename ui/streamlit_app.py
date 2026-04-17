import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from app.github import search_users, get_user_details, get_user_repos
from app.scoring import score_user
from app.enrichment import infer_roles
from app.integration import send_to_careergenie

# -----------------------------
# PAGE CONFIG (IMPORTANT)
# -----------------------------
st.set_page_config(
    page_title="CareerGenie",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "saved_candidates" not in st.session_state:
    st.session_state.saved_candidates = []

if "candidates" not in st.session_state:
    st.session_state.candidates = []

# -----------------------------
# HEADER
# -----------------------------
st.markdown("## 🚀 CareerGenie Talent Discovery")
st.caption("Find, evaluate, and invite top developers from GitHub")

# -----------------------------
# SIDEBAR (FILTERS)
# -----------------------------
st.sidebar.header("🔍 Filters")

language = st.sidebar.selectbox(
    "Programming Language",
    ["", "python", "javascript", "java", "go", "typescript"]
)

location = st.sidebar.text_input("Location")

min_followers = st.sidebar.slider("Min Followers", 0, 500, 10)
min_repos = st.sidebar.slider("Min Repos", 0, 100, 5)

search_clicked = st.sidebar.button("Search")

# -----------------------------
# QUERY BUILDER
# -----------------------------
def build_github_query(language, location, min_followers, min_repos):
    query = []
    if language:
        query.append(f"language:{language}")
    if location:
        query.append(f"location:{location.lower()}")
    if min_followers:
        query.append(f"followers:>{min_followers}")
    if min_repos:
        query.append(f"repos:>{min_repos}")
    return " ".join(query)

# -----------------------------
# SEARCH
# -----------------------------
if search_clicked:

    with st.spinner("🔎 Searching candidates..."):

        query = build_github_query(language, location, min_followers, min_repos)
        st.info(f"Query: {query}")

        users = search_users(query)

    if not users:
        st.warning("No candidates found. Try different filters.")
        st.stop()

    candidates = []

    for u in users:
        details = get_user_details(u["login"])
        repos = get_user_repos(u["login"])

        score = score_user(details, repos)
        roles = infer_roles(repos)

        candidates.append({
            "username": u["login"],
            "score": score,
            "roles": roles,
            "url": details.get("html_url")
        })

    st.session_state.candidates = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )

# -----------------------------
# MAIN DISPLAY
# -----------------------------
candidates = st.session_state.candidates

if candidates:

    st.markdown("### 🎯 Top Matches")

    top_score = candidates[0]["score"]

    for c in candidates:

        is_top = c["score"] >= top_score * 0.9

        # Card container
        with st.container():
            col1, col2 = st.columns([3, 1])

            with col1:
                if is_top:
                    st.markdown(f"### ⭐ {c['username']}")
                else:
                    st.markdown(f"### {c['username']}")

                st.markdown(f"**Score:** `{c['score']}`")

                st.markdown("**Roles:** " + ", ".join(c["roles"]))

                st.markdown(f"[View GitHub Profile]({c['url']})")

                # Message box
                message = st.text_area(
                    "Message",
                    value=f"Hi {c['username']}, I came across your GitHub and was impressed by your work.",
                    key=f"msg_{c['username']}"
                )

            with col2:
                st.metric("Score", c["score"])

                if st.button("Invite", key=f"invite_{c['username']}"):
                    candidate_with_msg = {**c, "message": message}

                    st.session_state.saved_candidates.append(candidate_with_msg)

                    send_to_careergenie(candidate_with_msg)

                    st.success("Invited ✅")

            st.divider()

# -----------------------------
# SIDEBAR - SAVED
# -----------------------------
st.sidebar.markdown("---")
st.sidebar.header("📌 Saved Candidates")

if st.session_state.saved_candidates:
    for c in st.session_state.saved_candidates:
        st.sidebar.markdown(f"**{c['username']}** ({c['score']})")
        st.sidebar.caption(c.get("message", ""))
        st.sidebar.markdown("---")
else:
    st.sidebar.write("No saved candidates yet.")

# -----------------------------
# EXPORT
# -----------------------------
if candidates:
    df = pd.DataFrame(candidates)
    csv = df.to_csv(index=False)

    st.download_button(
        "⬇ Export CSV",
        csv,
        "candidates.csv",
        "text/csv"
    )
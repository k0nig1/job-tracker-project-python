import streamlit as st
import os
import pandas as pd
from fetch_jobs import fetch_jobs
from resume_parser import parse_resume
from match_jobs import match_jobs_to_resume
from report_generator import generate_report

st.set_page_config(page_title="Job Match Tracker", layout="centered")

st.title("📄 Job Match Tracker")
st.markdown("Upload your resume and select job boards to find matching positions.")

selected_sites = st.multiselect(
    "Select job boards to search:",
    ["RemoteOK", "WeWorkRemotely", "StackOverflow Jobs", "HackerNews Jobs"],
    default=["RemoteOK"]
)

uploaded_file = st.file_uploader("Upload your resume (PDF only):", type=["pdf"])

if st.button("Run Job Match"):
    if not uploaded_file:
        st.warning("Please upload a resume.")
    elif not selected_sites:
        st.warning("Please select at least one job site.")
    else:
        os.makedirs("data", exist_ok=True)
        resume_path = "data/resume.pdf"
        if "resume_saved" not in st.session_state:
            with open(resume_path, "wb") as f:
                f.write(uploaded_file.read())
            st.session_state.resume_saved = True

        if "jobs" not in st.session_state:
            st.info("Fetching jobs...")
            st.session_state.jobs = fetch_jobs(title="developer", location="remote")
        jobs = st.session_state.jobs

        if "resume_keywords" not in st.session_state:
            st.info("Parsing resume...")
            st.session_state.resume_keywords = parse_resume(resume_path)
        resume_keywords = st.session_state.resume_keywords

        if "matched_jobs" not in st.session_state:
            st.info("Matching jobs...")
            st.session_state.matched_jobs = match_jobs_to_resume(jobs, resume_keywords)
        matched_jobs = st.session_state.matched_jobs

        st.info("Generating report...")
        report_path = "data/report.csv"
        generate_report(matched_jobs, report_path)

        st.success("✅ Job match complete!")

        df = pd.read_csv(report_path)
        df_display = df.sort_values(by="match_score", ascending=False).reset_index(drop=True)

        st.markdown("### 🎯 Filter by Minimum Match Score")
        min_score = st.slider("Minimum Match Score (%)", 0, 100, 50)

        filtered_df = df_display[df_display["match_score"] >= min_score]

        st.markdown("### 🔍 Top Matching Jobs")

        # Create clickable links
        filtered_df['Job Link'] = filtered_df['url'].apply(lambda x: f"[View Posting]({x})")

        # Select and rename columns
        display_df = filtered_df[['title', 'company', 'location', 'match_score', 'Job Link']]
        display_df.columns = ['Title', 'Company', 'Location', 'Match Score (%)', 'Link']

        # Show as markdown-rendered table
        st.write(display_df.to_markdown(index=False), unsafe_allow_html=True)

        with open(report_path, "rb") as f:
            st.download_button("📥 Download Report CSV", f, file_name="report.csv", mime="text/csv")
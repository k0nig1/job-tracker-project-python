import logging

def match_jobs_to_resume(jobs, resume_keywords):
    matched_jobs = []

    for job in jobs:
        job_text = f"{job.get('title', '')} {job.get('description', '')} {' '.join(job.get('tags', []))}".lower()
        job_words = set(job_text.split())
        matched_keywords = job_words.intersection(resume_keywords)
        match_score = len(matched_keywords) / len(resume_keywords) if resume_keywords else 0

        job['match_score'] = round(match_score * 100, 2)
        job['matched_keywords'] = list(matched_keywords)
        job['missing_keywords'] = list(set(resume_keywords) - matched_keywords)
        matched_jobs.append(job)

    logging.info(f'Matched {len(matched_jobs)} jobs with resume keywords.')
    return matched_jobs
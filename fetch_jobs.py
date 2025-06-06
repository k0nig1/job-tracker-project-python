

import requests
import logging
import json

API_URL = 'https://remoteok.io/api'

def fetch_jobs(title='', location=''):
    try:
        response = requests.get(API_URL, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        jobs = response.json()

        # RemoteOK includes a metadata header as the first item
        if jobs and isinstance(jobs, list):
            jobs = jobs[1:]

        filtered_jobs = []
        for job in jobs:
            job_title = job.get('position', '').lower()
            job_location = job.get('location', '').lower()

            if title.lower() in job_title and location.lower() in job_location:
                filtered_jobs.append({
                    'id': job.get('id'),
                    'title': job.get('position'),
                    'company': job.get('company'),
                    'location': job.get('location'),
                    'description': job.get('description'),
                    'tags': job.get('tags'),
                    'url': job.get('url')
                })

        with open('data/jobs.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_jobs, f, indent=2)

        logging.info(f'Fetched {len(filtered_jobs)} job listings.')
        return filtered_jobs

    except requests.RequestException as e:
        logging.error(f'Error fetching jobs: {e}')
        return []
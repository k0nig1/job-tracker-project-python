import argparse
import logging

from fetch_jobs import fetch_jobs
from resume_parser import parse_resume
from match_jobs import match_jobs_to_resume
from report_generator import generate_report

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description='Job Market Tracker & Resume Optimizer')
    parser.add_argument('--resume', type=str, required=True, help='Path to the resume PDF file')
    parser.add_argument('--output', type=str, default='data/report.csv', help='Path to save the output report')
    parser.add_argument('--location', type=str, default='', help='Location filter for job search')
    parser.add_argument('--title', type=str, default='', help='Job title filter')

    args = parser.parse_args()

    logging.info('Fetching job listings...')
    jobs = fetch_jobs(title=args.title, location=args.location)

    logging.info('Parsing resume...')
    resume_keywords = parse_resume(args.resume)

    logging.info('Matching jobs...')
    matched_jobs = match_jobs_to_resume(jobs, resume_keywords)

    logging.info('Generating report...')
    generate_report(matched_jobs, args.output)

    logging.info(f'Report saved to {args.output}')

if __name__ == '__main__':
    main()
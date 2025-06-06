import pandas as pd
import logging

def generate_report(matched_jobs, output_path):
    try:
        df = pd.DataFrame(matched_jobs)
        selected_columns = ['title', 'company', 'location', 'match_score', 'url', 'matched_keywords', 'missing_keywords']
        df = df[selected_columns]
        df.sort_values(by='match_score', ascending=False, inplace=True)

        df.to_csv(output_path, index=False)
        logging.info(f'Report successfully written to {output_path}')
    except Exception as e:
        logging.error(f'Error generating report: {e}')
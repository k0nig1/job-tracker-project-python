import fitz  # For extracting text from PDF resumes
import re
import logging

def parse_resume(resume_path):
    try:
        with fitz.open(resume_path) as doc:
            text = ''
            for page in doc:
                text += page.get_text()

        # Basic cleanup
        text = re.sub(r'\s+', ' ', text).lower()

        # Very simple keyword extraction (can be replaced with NLP later)
        words = re.findall(r'\b[a-z]{2,}\b', text)
        common_words = set([
            'the', 'and', 'for', 'with', 'you', 'your', 'this', 'that', 'have', 'from', 'will',
            'are', 'was', 'can', 'has', 'all', 'any', 'but', 'not', 'our', 'use', 'how', 'who',
            'where', 'when', 'why', 'also', 'their', 'more', 'these', 'such', 'each', 'should',
            'must', 'other', 'may', 'some', 'those', 'on', 'at', 'by', 'if', 'it', 'is', 'be', 'do', 'so', 'up', 'out', 'about', 'as', 'into',
            'than', 'like', 'over', 'after', 'before', 'between', 'during', 'while', 'through',
            'against', 'without', 'within', 'along', 'across', 'around', 'among', 'beyond', 'down',
            'into', 'onto', 'past', 'since', 'until', 'upon', 'within', 'without', 'above', 'below',
            'here', 'there', 'where', 'when', 'why', 'how', 'what', 'which', 'who', 'whom', 'whose',
            'if', 'then', 'else', 'although', 'because', 'since', 'unless', 'while', 'whereas', 'despite',
            'although', 'even', 'though', 'wherever', 'whenever', 'wherein', 'whereby', 'whereupon',
            'wherever', 'whenever', 'wherein', 'whereby', 'whereupon', 'whether', 'why', 'whoever',
            'whomever', 'whichever', 'whatever', 'whoever', 'whomever', 'whichever', 'whatever'
        ])
        keywords = sorted(set(words) - common_words)

        logging.info(f'Extracted {len(keywords)} keywords from resume.')
        return keywords

    except Exception as e:
        logging.error(f'Error parsing resume: {e}')
        return []
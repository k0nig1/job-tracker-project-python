# Job Market Tracker & Resume Optimizer

This Python project helps you automate the process of tracking job postings and analyzing how well your resume matches the requirements of each listing. It fetches jobs from RemoteOK, parses your resume, and generates a match report showing how closely each job aligns with your skills.

## 🚀 Features

- Fetch remote job listings via RemoteOK API
- Extract keywords from your resume (PDF)
- Match job descriptions to your resume keywords
- Generate a CSV report sorted by match score
- Easily customizable and testable

## 🧰 Technologies Used

- Python 3
- requests
- pandas
- PyMuPDF (fitz)
- matplotlib (optional for future visualizations)
- click & argparse
- pytest

## 📦 Installation

```bash
git clone https://github.com/yourusername/job-tracker-project-python.git
cd job-tracker-project-python
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 📝 Usage

```bash
python main.py --resume data/resume.pdf --output data/report.csv --title developer --location remote
```

- `--resume`: Path to your resume PDF
- `--output`: Path to save the job match report
- `--title`: Filter job listings by title (e.g., `developer`)
- `--location`: Filter job listings by location (e.g., `remote`)

## ✅ Example Output

A CSV report with:
- Job title, company, location
- Match score (percentage)
- Matching and missing keywords
- Job listing URL

## 🧪 Running Tests

```bash
pytest tests/
```

## 📁 Project Structure

```
├── main.py
├── fetch_jobs.py
├── resume_parser.py
├── match_jobs.py
├── report_generator.py
├── requirements.txt
├── README.md
├── data/
│   ├── resume.pdf
│   ├── jobs.json
│   └── report.csv
└── tests/
    ├── test_fetch_jobs.py
    ├── test_resume_parser.py
    ├── test_match_jobs.py
    └── test_report_generator.py
```

## 🔧 To-Do

- Add visualization dashboard (e.g., Dash or Streamlit)
- Add NLP-based keyword extraction (spaCy or NLTK)
- Add support for multiple job boards

## 📄 License

MIT License

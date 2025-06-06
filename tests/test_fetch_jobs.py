import pytest
from fetch_jobs import fetch_jobs
import requests
from unittest.mock import patch

mock_response_data = [
    {"id": 0},  # metadata item
    {
        "id": 1,
        "position": "Python Developer",
        "company": "Tech Co",
        "location": "Remote",
        "description": "Great job for Python developers",
        "tags": ["Python", "Developer"],
        "url": "https://example.com/job/1"
    },
    {
        "id": 2,
        "position": "Java Developer",
        "company": "Dev Corp",
        "location": "Onsite",
        "description": "Java dev role",
        "tags": ["Java"],
        "url": "https://example.com/job/2"
    }
]

@patch('fetch_jobs.requests.get')
def test_fetch_jobs_returns_filtered_jobs(mock_get):
    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return mock_response_data

    mock_get.return_value = MockResponse()

    jobs = fetch_jobs(title='python', location='remote')
    assert isinstance(jobs, list)
    assert len(jobs) == 1
    assert jobs[0]['title'] == 'Python Developer'
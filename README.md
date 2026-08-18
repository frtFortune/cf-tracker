# CF Tracker

A Python-based Codeforces progress tracker that collects a user's Codeforces activity and turns it into useful statistics about their competitive programming progress.

## Project Goal

CF Tracker is being built as a personal competitive programming tracking tool.

The project will start as a small, well-tested Python application and gradually evolve into a more complete tracking platform.

The main priorities are:

- Clean architecture
- Automated testing
- Useful Codeforces statistics
- Clear separation between API communication, application logic, and data storage
- A codebase that can grow without unnecessary complexity

## Development Roadmap

### Version 1 — Core Tracker

Build the foundation and the first usable version of the tracker.

Planned work:

- Codeforces API client
- Persistent storage
- Synchronize Codeforces submissions
- Track solved problems
- Track problem tags and ratings
- Calculate basic progress statistics
- Automated tests
- Basic documentation

### Version 2 — Tracking Interface

Build an interface for viewing the information collected by Version 1.

Planned work:

- User-facing dashboard
- Problem history
- Progress statistics
- Tag and rating breakdowns
- Improved filtering and searching
- More comprehensive testing
- Deployment

### Version 3 — Advanced Analysis

Add features that make the tracker more useful for improving competitive programming performance.

Potential work:

- Historical progress analysis
- Rating and performance trends
- Weak-topic identification
- Personalized problem recommendations
- Additional competitive programming insights

The scope of later versions may change as Version 1 and Version 2 reveal what is actually useful.

## Current Status

**Version 1 — In development**

Completed:

- Project/package setup
- Codeforces API client
- User information fetching
- User submission fetching
- API error handling
- Automated API-client tests
- API-client documentation

Current branch:

`feature/codeforces-api`

## Tech Stack

- Python
- HTTPX
- Pytest
- Codeforces API

Additional technologies will be introduced only when they are needed by the project.

## Project Structure

```text
cf-tracker/
├── cf_tracker/
│   ├── api/
│   │   └── codeforces.py
│   └── __init__.py
├── tests/
│   └── test_codeforces.py
├── pyproject.toml
├── .gitignore
└── README.md

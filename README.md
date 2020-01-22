# Food Truck Finder

Author: Steven Dang

## Requirements

- Python 3.6>
- pip3 (unless using virtual environment)
- appetite

## Setup

1. (Optional) Activate virtualenv `source venv/bin/activate`
2. Install dependencies `pip install requirements.txt`
3. Run Code `python show_open_food_trucks.py`

## Scaling the application

- Serializing responses into objects for maintanability

- Caching responses in distributed cache to reduce redundant calls to the API and continue filtering within the application. TTL designated by business needs.

- Unit tests and regression tests to thoroughly test capabilities

- Containerized with environment configurations to build, deploy, and horizontally scale quickly

- Place behind production grade HTTP server (ie: Nginx + Gunicorn) to serve up higher traffic and enable https


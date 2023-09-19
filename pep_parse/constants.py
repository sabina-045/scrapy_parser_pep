from pathlib import Path


DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://' + url + '/' for url in ALLOWED_DOMAINS]

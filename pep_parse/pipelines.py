from collections import defaultdict
import datetime as dt
import json

from .constants import DATETIME_FORMAT, BASE_DIR, RESULTS


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_collection = defaultdict(int)

    def process_item(self, item, spider):
        self.status_collection[item['status']] += 1
        return item

    def close_spider(self, spider):
        date_time = dt.datetime.now().strftime(DATETIME_FORMAT)
        total = sum(self.status_collection.values())
        results_dir = BASE_DIR / RESULTS
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / f'status_summary_{date_time}.csv'
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write(f'Статус,Количество\n'
                    f'Total, {total}\n'
                    f'{json.dumps(self.status_collection, indent=0)}\n')

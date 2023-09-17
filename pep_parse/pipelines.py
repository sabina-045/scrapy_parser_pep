from collections import defaultdict
import datetime as dt

from .constants import DATETIME_FORMAT


class PepParsePipeline:
    status_collection = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_collection[item['status']] += 1
        return item

    def close_spider(self, spider):
        date_time = dt.datetime.now().strftime(DATETIME_FORMAT)
        total = sum(self.status_collection.values())
        file_path = f'results/status_summary_{date_time}.csv'
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            f.write(f'Total, {total}\n')
            for key, value in self.status_collection.items():
                f.write(f'{key}, {value}\n')

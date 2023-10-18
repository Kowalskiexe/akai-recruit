import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        with open('ratios.json', 'r') as f:
            cache = json.load(f)
        for record in cache:
            if record['base_currency'] == self.base and record['target_currency'] == self.target:
                diff = datetime.datetime.now() - datetime.datetime.fromisoformat(record['date_fetched'])
                return diff.days < 1
        return False

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        with open('.SECRET') as f:
            SECRET = f.read().replace('\n', '')
        request = f'http://api.exchangerate.host/convert?access_key={SECRET}&from={self.base}&to={self.target}&amount=1'
        with urllib.request.urlopen(request) as resp:
            data = json.load(resp)
            self.save_ratio(data['result'])

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        with open('ratios.json', 'r') as f:
            cache = json.load(f)
        found = False
        for record in cache:
            if record['base_currency'] == self.base and record['target_currency'] == self.target:
                record['ratio'] = ratio
                record['date_fetched'] = str(datetime.date.today())
                found = True
                break
        if not found:
            record = {
                    'base_currency': self.base,
                    'target_currency': self.target,
                    'date_fetched': str(datetime.date.today()),
                    'ratio' : ratio
                    }
            cache.append(record)
        with open('ratios.json', 'w') as f:
            json.dump(cache, f, indent='\t')


    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open('ratios.json', 'r') as f:
            cache = json.load(f)
        for record in cache:
            if record['base_currency'] == self.base and record['target_currency'] == self.target:
                return record['ratio']

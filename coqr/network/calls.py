import argparse
import json
import os

import requests

from coqr.utils.encoder import JSONSerializer
from coqr.utils.file import read_json_file

parser = argparse.ArgumentParser(description='Sends data to server')

parser.add_argument('file')


def send_reports(reports):
    headers = {'Authorization': 'Token %s' % os.environ.get('TOKEN')}
    request = requests.post(os.environ.get('API_CREATE_REPORTS'), headers=headers,
                            json=json.loads(json.dumps(reports, cls=JSONSerializer)))
    request.raise_for_status()


if __name__ == '__main__':
    options = parser.parse_args()

    reports = read_json_file(options.file)
    send_reports(reports)

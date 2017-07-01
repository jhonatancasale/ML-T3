#!env python3
# -*- coding: utf-8 -*-

import logging
import sys
import requests
import os.path

logging.basicConfig(filename='history.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s'
                   )

BASE_YEAR = 2016

def main():
    '''Retrieve some data from http://www.fuvest.br'''

    range_years = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    years = list(range(BASE_YEAR, BASE_YEAR - range_years, -1))
    logging.debug('Trying to get data of the last %d years', range_years)

    for year in years:
        common_url = 'http://www.fuvest.br/vest{0}/download/FUVEST_{0}_qase_{1}_car_fuvest_{0}.pdf'
        urls = [common_url.format(year, phase) for phase in ['inscr', 'conv', '1matr']]
        for url in urls:
            logging.debug('Request year: %d to server', year)

            filename = url.split('/')[-1]
            if os.path.isfile(filename):
                logging.debug('Skiping this, file already exists')
                continue

            try:
                data = requests.get(url, stream=True)
            except FileNotFoundError as e:
                logging.debug('Fails because of %s', e)
            else:
                logging.debug('Done!')

            logging.debug('Saving data on file %s', filename)
            try:
                f = open(filename, 'wb')
                f.write(data.content)
                f.close()
            except IOError as e:
                logging.debug('Fails because of %s', e)
            else:
                logging.debug('Done!')

    logging.debug('Finished')


if __name__ == '__main__':
    main()

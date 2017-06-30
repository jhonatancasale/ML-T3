#!env python3
# -*- coding: utf-8 -*-

import click
import logging
import sys
import requests
import os.path
import glob
import re

#logging.basicConfig(filename='history.log', level=logging.DEBUG,
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s'
                   )

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
PATH_MSG = 'Try to load pdf files from <path>.'
OUTPUT_MSG = 'Place output files on <path> in csv format.'

FEATURES = '''Career, Year, 1.1, 1.2, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 9.1, 9.2, 9.3, 9.4, 9.5, 10.1, 10.2, 10.3, 10.4, 10.5, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 14.9, 15.1, 15.2, 15.3, 15.4, 15.5, 15., 15.7, 15.8, 15.9, 16.1, 16.2, 16.3, 16.4, 17.1, 17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 18.1, 18.2, 18.3, 18.4, 18.5, 18.6, 18.7, 18.8, 18.9, 18.10, 18.11, 19.1, 19.2, 19.3, 19.4, 19.5, 20.1, 20.2, 20.3, 20.4, 20.5, 21.1, 21.2, 21.3, 21.4, 21.5, 21.6, 21.7, 22.1, 22.2, 22.3, 22.4, 22.5, 22.6, 23.1, 23.2, 23.3, 23.4, 23.5, 24.1, 24.2, 25.1, 25.2, 25.3, 25.4, 25.5, 26.1, 26.2, 26.3, 26.4, 26.5, 27.1, 27.2, 27.3, 27.4, 27.5, 27.6, 28.1, 28.2, 29.1, 29.2, 30.1, 30.2, 31.1, 31.2, 32.1, 32.2, 32.3, 32.4, 32.5, 32.6, 32.7, 32.8, 33.1, 33.2, 33.3, 33.4, 33.5, 34.1, 34.2, 34.3, 34.4, 34.5, 34.6'''.split(', ')

FEATURES_SIZE = len(FEATURES)

def get_year(filename):
    return int(filename[-4:])


def get_filename(fullname):
    return fullname.split('/')[-1][:-4]

def get_career_info(data):
    while True:
        line = data.readline()
        if 'Candidatos que se inscreveram' in line:
            line = data.readline()
            total, partial = re.search('Dos (\d+)(\D+), (\d+)', line).group(1, 3)
            career = line.split(',')[2].replace('−', ' - ').replace('  ', ' ')

            return (career, total, partial) 


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-p', '--path', default='./', help=PATH_MSG, metavar='<path>')
@click.option('-o', '--output', default='./', help=OUTPUT_MSG, metavar='<path>')
def main(**kwargs):
    """Convert any csv file on 'path' to a single pandas.DataFrame and save then on 'output'"""


    path = kwargs['path']
    output = kwargs['output']

    logging.debug('Loading pdf files from %s', path)
    files = glob.glob(path + '*.csv')

    probs = []
    for _file in files:
        logging.debug('Loading %s', _file)
        filename = get_filename(_file)
        year = get_year(filename)

        with open(_file, newline='') as data:
            while True:
                probs = []
                career, total, partial_people = get_career_info(data)
                logging.debug('Grabbing stats for %s', career)
                probs.append(career)
                probs.append(year)

                while True:
                    line = data.readline()
                    partial = re.search('\((\d+)\)', line)

                    if partial is not None:
                        probs.append(partial.group(1))

                    if len(probs) == FEATURES_SIZE:
                        print(probs)
                        break

                if career == 'Total das Carreiras':
                    break
        logging.debug('Adding to DataFrame')
    logging.debug('Finished')


if __name__ == '__main__':
    main()

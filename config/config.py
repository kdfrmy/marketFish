import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_config(section, key):
    conf = configparser.ConfigParser()
    conf.read(os.path.join(BASE_DIR, 'config.ini'))
    tushare_token = conf.get(section, key)
    return tushare_token


if __name__ == '__main__':
    print(get_config("token", "tushare-token"))

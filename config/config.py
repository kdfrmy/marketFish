import configparser


def get_config(section, key):
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    tushare_token = conf.get(section, key)
    return tushare_token

"""
定时更新任务，获取基本信息
"""
import tushare as ts
import pickle
from pypinyin import lazy_pinyin
import pathlib
from config import config


class SaveLoadPickle:
    def __init__(self):
        ts.set_token(config.get_config("token", "tushare-token"))
        pro = ts.pro_api()
        self.pro = pro
        self.pickle_file_name = "stock_basic_info.pkl"

    def save_basic_info_pickle(self):
        """
        DataFrame存储在pickle文件中
        data格式：
            ts_code    symbol  name  area   industry list_date short
        0    XXX.SZ  000000  XXXX   深圳       XX  19910403  payh
        """
        data = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        data['short'] = data['name'].apply(lambda nm: self.solve_pinyin(nm))
        # print(data.head(3))
        with open(self.pickle_file_name, "wb") as info_file:
            pickle.dump(data, info_file)

    def load_basic_info_pickle(self):
        """
        加载数据，无数据文件时生成pickle文件
        """
        if not pathlib.Path(self.pickle_file_name).exists():
            self.save_basic_info_pickle()

        with open(self.pickle_file_name, "rb") as info_file:
            loaded_data = pickle.load(info_file)
            return loaded_data

    @staticmethod
    def solve_pinyin(name):
        """
        :param
            name: 名称
        :return
            返回小写拼音的首字母缩写 如：ymd
        """
        return "".join([p[0].lower() for p in lazy_pinyin(name)])


if __name__ == "__main__":
    basic = SaveLoadPickle()
    # data = basic.load_basic_info_pickle()
    basic.save_basic_info_pickle()
    # print(data.head())

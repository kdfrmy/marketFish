import argparse

from util import paint
from util import tty_menu
from util.basic_info import TushareFish


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--price', required=False, help="当前行情")
    parser.add_argument('-n', '--north', required=False, action='store_true', help="北上资金")  # 不带参数值
    parser.add_argument('-s', '--south', required=False, action='store_true', help="南下资金")  # 不带参数值
    parser.add_argument('-d', '--index', required=False, action='store_true', help="上证指数")  # 不带参数值
    parser.add_argument('-m', '--main', required=False, help="主营业务")
    return parser


def resolve_param(param):
    """
    解析选项带值参数 比如 -p zxjt
    """
    if param.isalpha():
        return get_pickle_symbol(param, "short")
    elif param.isdigit():
        return get_pickle_symbol(param, "symbol")
    elif is_chinese(param):
        return get_pickle_symbol(param, "name")
    else:
        raise Exception("参数错误")


def alternative_list(pair_df):
    """
    返回备选列表
    """
    return [z[0] + "\t" + z[1] for z in zip(pair_df['symbol'], pair_df['name'])]


def get_pickle_symbol(param, field):
    """
    根据传入参数返回symbol字段及附加中文名字段，传入参数为字母或者中文
    :params
        param: 搜索参数
        filed：name、short、symbol字符串
    """
    fish = TushareFish()
    data = fish.load_basic_info_pickle()
    return data[data[field] == param][['symbol', 'name']]


def is_chinese(word):
    """
    判断字符串是否为中文
    """
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def resolve_current_price(param):
    """
    对参数-p的解析，显示现价行情
    """
    if len(param) >= 2:
        select = alternative_list(param)
        menu = tty_menu.tty_menu(select, title='请选择?')
        selected = select[menu]
        code = selected.split('\t')[0]
        name = selected.split('\t')[1]
        paint.print_tick(code, name)
    elif len(param) == 1:
        code = param['symbol'].iloc[0]
        name = param['name'].iloc[0]
        paint.print_tick(code, name)


def resolve_main_business_param(param):
    resolved_param_m = resolve_param(param)
    if len(resolved_param_m) >= 2:
        select = alternative_list(resolved_param_m)
        menu = tty_menu.tty_menu(select, title='请选择?')
        selected = select[menu]
        code = selected.split('\t')[0]
        return pick_main_business(code)
    elif len(resolved_param_m) == 1:
        code = resolved_param_m['symbol'].iloc[0]
        return pick_main_business(code)


def pick_main_business(code):
    """
    :params:
        code: 形如600123
    :return:
        返回 600123.SH 或者 000123.SZ的形式
    """
    fish = TushareFish()
    data = fish.load_basic_info_pickle()
    code_end_with_sh_hz = data[data['symbol'] == code].iloc[0]['ts_code']
    return fish.main_business(code_end_with_sh_hz)

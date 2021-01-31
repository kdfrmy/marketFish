"""
画图以及打印
"""
from util.remote_data import get_current_price, resolve_json, get_north, get_sh000001,get_south

BOLD = "\033[1m"  # 加粗
PROPERTY_END = "\033[0m"  # 属性设置结束
COLOR_RED = "\033[31m"  # 红色
COLOR_GREEN = "\033[32m"  # 绿色


def print_north_capital():
    """
    打印北上资金情况
    """
    north_capital = get_north()
    print("净流入\t沪股通\t深股通")
    net = north_capital.sh_channel.net_in + north_capital.sz_channel.net_in
    paint_capital(net, north_capital)


def print_south_capital():
    """
    打印北上资金情况
    """
    south_capital = get_south()
    print("净流入\t港股通-上海\t港股通-深圳")
    net = south_capital.sh_channel.net_in + south_capital.sz_channel.net_in
    paint_capital(net, south_capital)


def paint_capital(net, south_capital):
    """
    打印资金，北上和南下
    """
    color_net = get_color(net)
    color_sh = get_color(south_capital.sh_channel.net_in)
    color_sz = get_color(south_capital.sz_channel.net_in)
    print(color_net + str(round(net / 10000, 2)) + '亿' + '\t' + PROPERTY_END
          + color_sh + str(round(south_capital.sh_channel.net_in / 10000, 2)) + '亿' + '\t' + PROPERTY_END
          + color_sz + str(round(south_capital.sz_channel.net_in / 10000, 2)) + '亿' + '\t' + PROPERTY_END)


def get_color(number):
    return COLOR_RED if number >= 0 else COLOR_GREEN


def print_tick(code, name):
    """
    打印现价行情
    """
    response = get_current_price(code)
    tick = resolve_json(response)
    print("code\tname\trise\tcurrent\topen\thigh\tlow")
    if tick.rising_rate_i >= 0:
        # \033[1m 加粗
        # \033[31m 字体颜色红  \033[32m 字体颜色绿
        # \033[0m 结束属性设置
        # code name 无色
        print(
            BOLD + code + "\t" + name + "\t" + COLOR_RED + tick.rising_rate + "\t" + tick.close + "\t" + tick.open
            + "\t" + tick.high
            + "\t" + tick.low + PROPERTY_END)
    else:
        print(
            BOLD + code + "\t" + name + "\t" + COLOR_GREEN + tick.rising_rate + "\t" + tick.close + "\t" + tick.open
            + "\t" + tick.high
            + "\t" + tick.low + PROPERTY_END)


def print_index_sh():
    """
    打印上证指数情况
    """
    res = get_sh000001()
    tick = resolve_json(res)
    color = get_color(tick.rising_rate_i)
    print("点数" + "\t" + "涨幅")
    print(BOLD + color + str(round(float(tick.close), 2)) + '\t' + tick.rising_rate + PROPERTY_END)


if __name__ == '__main__':
    print_index_sh()

import urllib.request
from tick import Tick


def get_remote_price(code):
    prefix = "sh" if code.startswith('6') else "sz"
    url = "http://hq.sinajs.cn/list=" + prefix + code
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                     "like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    request.add_header("host", "hq.sinajs.cn")
    request.add_header("Referer", "http://finance.sina.com.cn/realstock/company/" + prefix + code + "/nc.shtml")
    response = str(urllib.request.urlopen(request).read())
    return response


def resolve_json(response):
    p_q = response.split(",")
    tick = Tick(open_p=p_q[1], close=p_q[3], high=p_q[4], low=p_q[5],
                rising_rate=round((float(p_q[3]) - float(p_q[2])) / float(p_q[2]), 4), )
    return tick


def get_stock_list():
    return []


def get_sh000001():
    url = "http://hq.sinajs.cn/list=sh000001"
    request = urllib.request.Request(url)
    request.add_header("host", "hq.sinajs.cn")
    request.add_header("referer", "http://finance.sina.com.cn/realstock/company/sh000001/nc.shtml")
    request.add_header("user-agent",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    response = str(urllib.request.urlopen(request).read())
    print(response)
    # TODO 今开 昨收 当前 最高 最低成交量手 成交额元  按规则解析


def print_tick(code, name):
    response = get_remote_price(code)
    tick = resolve_json(response)
    print("code\tname\trise\tcurrent\topen\thigh\tlow")
    if tick.rising_rate_i >= 0:
        # \033[1m 加粗
        # \033[31m 字体颜色红  \033[32m 字体颜色绿
        # \033[0m 结束属性设置
        # code name 无色
        print(
            "\033[1m" + code + "\t" + name + "\t" + "\033[31m" + tick.rising_rate + "\t" + tick.close + "\t" + tick.open + "\t" + tick.high
            + "\t" + tick.low + "\033[0m")
    else:
        print(
            "\033[1m" + code + "\t" + name + "\t" + "\033[32m" + tick.rising_rate + "\t" + tick.close + "\t" + tick.open + "\t" + tick.high
            + "\t" + tick.low + "\033[0m")

import urllib.request
from model.tick import Tick
import json
from model.capital_channel import CapitalChannel
from model.capital_channel import NorthCapitalChannel


def get_current_price(code):
    """
    获取现价
    """
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


def get_north():
    """
    获取北上资金信息
    """
    url = "http://push2.eastmoney.com/api/qt/kamt/get?fields1=f1,f2,f3,f4&fields2=f51,f52,f53,f54,f63"
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                     "like Gecko) Chrome/86.0.4240.111 Safari/537.36")
    request.add_header("host", "push2.eastmoney.com")
    request.add_header("Referer", "http://data.eastmoney.com/")
    response = urllib.request.urlopen(request).read()
    channel_data = json.loads(response)['data']
    hk2sh = CapitalChannel(net_buy=channel_data['hk2sh']['netBuyAmt'],
                           net_in=channel_data['hk2sh']['dayNetAmtIn'],
                           remain=channel_data['hk2sh']['dayAmtRemain'],
                           threshold=channel_data['hk2sh']['dayAmtThreshold'])
    hk2sz = CapitalChannel(net_buy=channel_data['hk2sz']['netBuyAmt'],
                           net_in=channel_data['hk2sz']['dayNetAmtIn'],
                           remain=channel_data['hk2sz']['dayAmtRemain'],
                           threshold=channel_data['hk2sz']['dayAmtThreshold'])
    return NorthCapitalChannel(hk2sh_channel=hk2sh, hk2sz_channel=hk2sz)


def get_sh000001():
    url = "http://hq.sinajs.cn/list=sh000001"
    request = urllib.request.Request(url)
    request.add_header("host", "hq.sinajs.cn")
    request.add_header("referer", "http://finance.sina.com.cn/realstock/company/sh000001/nc.shtml")
    request.add_header("user-agent",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/86.0.4240.111 Safari/537.36")
    return str(urllib.request.urlopen(request).read())
    # 今开 昨收 当前 最高 最低成交量手 成交额元  按规则解析

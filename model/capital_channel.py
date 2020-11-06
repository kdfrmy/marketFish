class CapitalChannel:
    """
    资金通道
    """

    def __init__(self, net_in, remain, net_buy, threshold):
        """
        :params
            net_in:净流入
            remain:当日余额
            net_buy:净买额
            threshold:买入限额
        """
        self.net_in = net_in
        self.remain = remain
        self.net_buy = net_buy
        self.threshold = threshold


class NorthCapitalChannel:
    """
    北向资金包括两个资金通道：
        沪股通: hk2sh
        深股通：hk2sz
    """

    def __init__(self, hk2sh_channel, hk2sz_channel):
        """
        :params
            hk2sh_channel: 沪股通
            hk2sz_channel: 深股通
        """
        self.sh_channel = hk2sh_channel
        self.sz_channel = hk2sz_channel


class SouthCapitalChannel:
    """
    南向资金包括两个资金通道：
        港股通-沪：sh2hk
        港股通-深：sz2hk
    """

    def __init__(self, sh2hk_channel, sz2hk_channel):
        self.hz_channel = sh2hk_channel
        self.sz_channel = sz2hk_channel

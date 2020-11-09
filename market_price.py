# coding=UTF-8
from util import args, remote_data

if __name__ == "__main__":

    parser1 = args.get_parser()
    known_args = parser1.parse_known_args()[0]
    if known_args.price is not None:
        resolved_p = args.resolve_param_p(known_args.price)
        args.resolve_current_price(resolved_p)
    elif known_args.north:
        remote_data.print_north_capital()
    # 其他选项在此添加
    else:
        res = remote_data.get_sh000001()

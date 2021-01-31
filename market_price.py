# coding=UTF-8
from util import args
from util import paint

if __name__ == "__main__":

    parser1 = args.get_parser()
    known_args = parser1.parse_known_args()[0]
    if known_args.price is not None:
        resolved_p = args.resolve_param(known_args.price)
        args.resolve_current_price(resolved_p)
    elif known_args.north:
        paint.print_north_capital()
    elif known_args.main is not None:
        main_business = args.resolve_main_business_param(known_args.main)
        print(main_business)
    elif known_args.south is not None:
        paint.print_south_capital()
    # 其他选项在此添加
    else:
        paint.print_index_sh()

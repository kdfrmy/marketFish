# marketFish

## Usage

### Step 1
由于使用了tushare库，需要配置token。<br>
在config文件夹，config.ini文件中配置tushare token<br>
tushare邀请链接<br>
https://tushare.pro/register?reg=337799<br> 

### Step 2
market_price.py [-h] [-p PRICE] [-m MAIN] [-b] [-d] <br>

optional arguments:<br>
  -h, --help            show this help message and exit<br>
  -p PRICE, --price PRICE    当前行情,参数支持中文全名、数字、拼音首字母<br>
  -b, --north           北上资金<br>
  -d, --index           上证指数<br>
  -m MAIN, --main MAIN  主营业务信息<br>
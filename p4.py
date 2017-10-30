import sys
import urllib
import re

def get_quote():
    symbol = format(sys.argv[0], '0004d')
    base_url = 'https://hk.finance.yahoo.com/lookup?s='
    content = urllib.urlopen(base_url + symbol +'.hk').read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    name = m.group(1)
    if m:
        quote = m.group(2)
        name = m.group(1)
    else:
        quote = symbol + ' is out of range!'
    print 'The price of ' + name + ' is ' + quote

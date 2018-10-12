# ip-tools

import sys
import requests


API_URL = 'https://api.ipify.org'
JSON_CMD = ['-j','--json']
JSONP_CMD = ['-jp','--jsonp']
CALLBACK_CMD = ['-c', '--callback']

def get_my_external_ipv4(format=None, callback=None):
    query_dict = {}

    if format == 'json':
        query_dict['format'] = 'json'
        return requests.get(API_URL, params=query_dict).json()

    elif format == 'jsonp':
        query_dict['format'] = 'jsonp'
        if callback:
            query_dict['callback'] = callback
        return requests.get(API_URL, params=query_dict).text

    else:
       return requests.get(API_URL).text


if __name__ == '__main__':
    argv = sys.argv
    format = None
    callback = None

    for arg in argv[1:]:
        if arg in JSON_CMD:
            format = 'json'
        elif arg in JSONP_CMD:
            format = 'jsonp'
        elif arg.split('=')[0] in CALLBACK_CMD:
            callback = arg.split('=')[1]
        else:
            print(f'Unknown argument {arg}.')

    if callback and format != 'jsonp':
        print('Argument "callback" will not processed!')

    my_ip = get_my_external_ipv4(format=format, callback=callback)
    print(my_ip)
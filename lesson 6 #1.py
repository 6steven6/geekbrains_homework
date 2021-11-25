from requests import get
import collections
response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

with open('nginx_logs.txt', 'w+',) as f:
    f.write(response)
    f.seek(0)
    for line in f:
        content = line.split()
        result = content[0], content[5], content[6]
        print(result)
        ip = content[0]

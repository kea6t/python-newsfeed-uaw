def format_date(date):
    return date.strftime('%m/%d/%y')

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

from datetime import datetime
print(format_date(datetime.now()))

print(format_url('http://google.com/test/'))
print(format_url('https://google.com?q=test'))
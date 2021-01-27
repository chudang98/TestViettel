from crawlData import crawl_data_cv, filter_cv
from sendMail import sendMail 

DELTA_DAY_TIME = 50
CV_URL = 'https://airtable.com/shr7Q4iNWosrNgxoH/tblHrgb8n4fNAHI4Q'

print('Đang tải và lọc dữ liệu...')
data = crawl_data_cv(CV_URL)

dataSend = filter_cv(data, DELTA_DAY_TIME)
for cv in dataSend:
    print(cv)

print('Đang gửi mail...')
sendMail(dataSend)
print('Đã gửi mail !')
from crawlData import crawl_data_cv, filter_cv
from sendMail import sendMail 

# Số ngày để  Last modified date ở đây em để là 50 ngày vì nếu để 2 tuần thì không có dữ liệu nào phù hợp. 
DELTA_DAY_TIME = 50
CV_URL = 'https://airtable.com/shr7Q4iNWosrNgxoH/tblHrgb8n4fNAHI4Q'

print('Đang tải dữ liêu...')
data = crawl_data_cv(CV_URL)

print('Dữ liệu các CV lấy về được')
for cv in data:
    print(cv)
print('Đang lọc dữ liệu')
dataSend = filter_cv(data, DELTA_DAY_TIME)

print('Đang gửi mail...')
sendMail(dataSend)
print('Đã gửi mail !')
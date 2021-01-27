# Bài test Viettel Cyber Security
## Cài đặt 

Cài đặt và chạy selenium/standalone-chrome trên Docker
```
$ docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:4.0.0-beta-1-prerelease-20210114
```


Sau khi clone repository, chuyển cmd vào môi trường của repository sau khi clone.
Cài đặt môi trường python riêng cho project
```
$ pip install virtualenv
$ virtualenv venv --python=python3.8
```

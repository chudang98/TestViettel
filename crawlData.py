from selenium import webdriver
import os
from datetime import date, timedelta, datetime

def filter_cv(list_cv, DELTA_DAY_TIME):
    today = datetime.today()
    result = list(filter(
        lambda cv: 
            (today - datetime.strptime(cv['lastDayModified'], '%m/%d/%Y')).days < DELTA_DAY_TIME
            and
            recognizeDev(cv) == True
        ,list_cv))
    return result

def recognizeDev(CV):
    keywords = ["dev", "developer", "backend", "frontend"]
    for word in keywords:
        if word in CV['position'].lower():
            return True
        if word in CV['note'].lower():
            return True
        if word in CV['pool'].lower():
            return True
    return False    


def crawl_data_cv(CV_URL):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        options=chrome_options
    )

    driver.set_window_size(3024, 5000)

    driver.get(CV_URL)

    pathName = "//body/div[@id='hyperbaseContainer']/div[@id='applicationContainer']/div[@id='table']/div[@id='view']/div[@id='gridView']/div[@id='paneContainer']/div[@id='headerAndDataRowContainer']/div[1]/div/div/div/div[2]/div[1]/div[1]"
    pathInfor = "//body/div[@id='hyperbaseContainer']/div[@id='applicationContainer']/div[@id='table']/div[@id='view']/div[@id='gridView']/div[@id='paneContainer']/div[@id='headerAndDataRowContainer']/div[3]/div[2]/div[1]/div"

    elements = driver.find_elements_by_xpath(pathInfor)
    names = driver.find_elements_by_xpath(pathName)

    del elements[-1]

    xpathProperties = [  
        {
            'xpath': "div[2]/div",
            'property': 'position'
        },
        {
            'xpath': "div[9]",
            'property': 'dateOfBirth'
        },
        {
            'xpath': "div[4]/div/div",
            'property': 'note'
        },
        {
            'xpath': "div[5]",
            'property': 'pool'
        },
        {
            'xpath': "div[6]",
            'property': 'whoCares'
        },

        {
            'xpath': "div[13]",
            'property': 'lastDayModified'
        },
              {
            'xpath': "div[1]/div/div/span",
            'property': 'linkCV'
        },
    ]

    array_name = []
    for name in names:
        array_name.append(name.text)

    array_result = []
    for index,element in enumerate(elements) :
        index_prop = 3
        data = {}
        data['name'] = array_name[index]
        for prop in xpathProperties:
            index_prop += 1
            try:
                # data.insert(index_prop, prop["property"], element.find_element_by_xpath(prop["xpath"]).text)
                data[prop["property"]]= element.find_element_by_xpath(prop["xpath"]).text
            except Exception:
                data[prop["property"]] = ""
        array_result.append(data)
    driver.close()
    return array_result
    

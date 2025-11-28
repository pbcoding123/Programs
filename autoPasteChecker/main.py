import time
from selenium import webdriver
import selenium

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

dr = webdriver.Chrome()
urlList = []
with open("url.txt", "r", encoding="utf-8") as f:
    urlList = f.read().split("\n")

print(urlList)

f = open("requests.txt", "w", encoding="utf-8")

for url in urlList:
    dr.get("https://www.luogu.com.cn/paste/"+url)
    time.sleep(0.25)
    try:
        dr.find_element("class name", "l-card")
        f.write(url+"   PasteBin Not Found!\n")
    except selenium.common.exceptions.NoSuchElementException as e:
        f.write(url+"   PasteBin Found!\n")

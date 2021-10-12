from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


def gcooter_crawling(search, search_limit):
    driver = webdriver.Chrome("C:/Users/quzmi/chromedriver.exe") # 본인 chromedriver 저장소
    driver.maximize_window()
    driver.get("https://www.google.co.kr/search?q=" + str(search) + "&hl=ko&tbm=isch")
    elem = driver.find_element_by_name("q")
#     elem.send_keys("지쿠터")
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 스크롤 끝까지 내리기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 1

    for i in range(search_limit+1):
        try:
            images[i].click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
            urllib.request.urlretrieve(imgUrl, "C:/Users/quzmi/crawling/211012/" + search + str(count) + ".jpg")
            # 데이터를 저장할 장소 설정
            count += 1
        except:
            pass

    driver.close()
    print(search+' 다운로드 완료')

search = input('검색하고 싶은 키워드: ')
search_limit = int(input('원하는 이미지 수집 개수 : '))
gcooter_crawling(search, search_limit)
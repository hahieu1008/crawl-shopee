from seleniumbase import Driver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = Driver(uc=True,
                    incognito=True)
sources = [
    "https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567",
    "https://shopee.vn/%C4%90i%E1%BB%87n-Tho%E1%BA%A1i-Ph%E1%BB%A5-Ki%E1%BB%87n-cat.11036030",
    "https://shopee.vn/Thi%E1%BA%BFt-B%E1%BB%8B-%C4%90i%E1%BB%87n-T%E1%BB%AD-cat.11036132",
    "https://shopee.vn/M%C3%A1y-T%C3%ADnh-Laptop-cat.11035954",
    "https://shopee.vn/M%C3%A1y-%E1%BA%A2nh-M%C3%A1y-Quay-Phim-cat.11036101"
]
listlink = []
for source in sources:

    driver.get(source)
    sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopee-category-list__toggle-btn")))
    elm = driver.find_element(By.CSS_SELECTOR, ".shopee-category-list__toggle-btn")
    elm.click()
    sleep(1)
    cats = driver.find_elements(By.CSS_SELECTOR, ".shopee-category-list__sub-category-list a")
    for cat in cats:
        i = 0
        for i in range(8):
            line = cat.get_attribute("href").split('-cat.')[1]+"_"+str(i)+"\n"
            i = i + 1
            listlink.append(line)
            #print(line)

textfile = open('cats.txt', 'w+', encoding="utf-8")
textfile.writelines(listlink)
textfile.close()
driver.close()
print("Done")
sleep(20)
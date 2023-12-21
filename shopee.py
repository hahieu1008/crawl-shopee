from seleniumbase import Driver
from time import sleep
from selenium.webdriver.common.by import By
import csv
import threading
import random

def run():
    d = 0
    while True:
        text_file = open("cats.txt", "r")
        cats = text_file.readlines()
        cat = random.choice(cats)

        text_file = open("skipcats.txt", "r")
        skipcats = text_file.readlines()
        if cat in skipcats:
            print("pass")
            continue
        else:
            print("run")

        item = cat.replace("\n","").split("_")
        url = "https://shopee.vn/z-cat."+item[0]+"?page="+item[1]
        print('Crawl: '+str(url))
        if d == 0:
            driver = Driver(uc=True, incognito=True)
            d = 1
        else:
            print("")
        driver.get(url)
        sleep(5)
        driver.execute_script("window.scrollTo(0, " + str(1200) + ");")
        a = 2
        for a in range(5):
            driver.execute_script("window.scrollTo(0, " + str(a * 1200) + ");")
            sleep(3)

        products = driver.find_elements(By.CLASS_NAME, 'shopee-search-item-result__item')

        i = 0
        arr_products = []
        err = 0
        for items in products:
            try:
                arritem = []
                # product_name
                title = items.find_element(By.CSS_SELECTOR, 'div[data-sqe="name"] > div').text
                arritem.append(title)

                # product_url
                url = items.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
                arritem.append(url)

                # product_rating
                try:
                    stars = items.find_elements(By.CSS_SELECTOR, '.shopee-rating-stars__lit')
                    point = 0
                    for star in stars:
                        point = point + float(star.get_attribute("style").replace("width: ", "").replace("%;", ""))
                    ratestar = round(point / 100, 1)
                except:
                    ratestar = -1
                arritem.append(ratestar)

                # product_price
                price = items.find_element(By.CSS_SELECTOR, '.k9JZlv').text
                price = price.replace(".", "")
                arritem.append(price)

                # product_revenue
                try:
                    history_sold = items.find_element(By.CSS_SELECTOR, '.JxvxgB .DN6Jp1 .OwmBnn').text
                    history_sold = history_sold.replace("Đã bán ", "").replace(",", "").replace("k", "00")
                    product_revenue = int(price) * int(history_sold)
                except:
                    product_revenue = 0
                arritem.append(product_revenue)

                i = i + 1
                arr_products.append(arritem)


            except:
                err = 1
                print("err")

        if err != 1 and len(arr_products) != 0:
            # .csv
            header = ['product_name', 'product_url', 'product_rating', 'product_price', 'product_revenue']
            name = cat.replace("\n", "")
            with open(str(name) + '.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(arr_products)

            with open("skipcats.txt", 'a') as file1:
                file1.write(cat)
        else:
            print("driver close")
            driver.close()
            d = 0
        #break


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=())
    t2 = threading.Thread(target=run, args=())
    t3 = threading.Thread(target=run, args=())
    t4 = threading.Thread(target=run, args=())
    t5 = threading.Thread(target=run, args=())
    t6 = threading.Thread(target=run, args=())
    t7 = threading.Thread(target=run, args=())
    t8 = threading.Thread(target=run, args=())
    t9 = threading.Thread(target=run, args=())
    t10 = threading.Thread(target=run, args=())
    # t11 = threading.Thread(target=run, args=())
    # t12 = threading.Thread(target=run, args=())
    # t13 = threading.Thread(target=run, args=())
    # t14 = threading.Thread(target=run, args=())
    # t15 = threading.Thread(target=run, args=())

    t1.start()
    sleep(3)
    t2.start()
    sleep(3)
    t3.start()
    sleep(3)
    t4.start()
    sleep(3)
    t5.start()
    sleep(3)
    t6.start()
    sleep(5)
    t7.start()
    sleep(5)
    t8.start()
    sleep(5)
    t9.start()
    sleep(5)
    t10.start()
    sleep(5)
    # t11.start()
    # sleep(5)
    # t12.start()
    # sleep(5)
    # t13.start()
    # sleep(5)
    # t14.start()
    # sleep(5)
    # t15.start()
    # sleep(5)

exit()

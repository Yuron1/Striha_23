from selenium import webdriver # скачиваем библиотеку селениум pip install seltnium
from selenium.webdriver.common.by import By # устанавливаем веб драйвер
from selenium.webdriver.common.keys import Keys #для эмуляции нажатия сочетаний клавиш передавайте их через параметры метода
from autch_data import username, password # импортирует пароль и код

import time # для создания паузы
import random



# def login(username, password):
#     browser = webdriver.Firefox(executable_path='firefoxdriver/geckodriver.exe')
#     путь к файлу драйвера
#     try: оборачиваем в трай на случай если инстаграм что то изменит в коде
#         browser.get('http://www.instagram.com') переходим на главную страницу
#         time.sleep(random.randrange(3, 5)) для загрузки страницы
#
#         username_input = browser.find_element(By.NAME, 'username') указываем путь к логину
#         username_input.clear() для очистки поля
#         username_input.send_keys(username)передаем логин в поле
#
#         time.sleep(2) пауза
#
#         password_input = browser.find_element(By.NAME, 'password')
#         password_input.clear()
#         password_input.send_keys(password)
#
#         password_input.send_keys(Keys.ENTER) эмулируем нажатие на ввод
#         time.sleep(10)
#
#
#         browser.close() закрывает вкладку в браузере
#         browser.quit()  закрывает сам браузер
#     except Exception as ex: при наличии ошибки закроется браузер
#         print(ex)
#         browser.close()
#         browser.quit()
#
#
# login(username, password)

def hashtag_search(username, password, hasgtag): # создаем функцию хештег
    browser = webdriver.Firefox(executable_path='firefoxdriver/geckodriver.exe')

    try:
        browser.get('http://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hasgtag}/') # копируем и вставляем ссылку с хештегом с главной страницы
            time.sleep(5)

            for i in range(1, 5): # количества проскроливаний
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # код для проскроливания страницы по всей высоте
                time.sleep(random.randrange(4,7))

            hrefs = browser.find_elements(By.TAG_NAME, 'a')

            posts_urls = [item.get_attribute('href') for item in hrefs if "/p/" in item.get_attribute('href')]
            #собираем все ссылки с постов ковка (условие в одной строке)


            # posts_urls = [] достаем в список ссылку с каждого элемента
            # for item in hrefs:
            #     href = item.get_attribute('href')
            #
            #     if "/p/" in href: обращаемся к ссылкам с элементом /p/
            #         posts_urls.append(href)
            #         print(href)

            for url in posts_urls: # пробегаем по каждой ссылке открываем и ставим лайк
                # также сдесь можно поставить условие как и сколько ссылок должны получатьлайки
                try:
                    browser.get(url)
                    time.sleep(3)
                    like_button = browser.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div['
                                                             '1]/div[1]/div[2]/section/main/div[1]/div['
                                                             '1]/article/div/div[2]/div/div[2]/section[1]/span['
                                                             '1]/button').click()
                    # переход по каждой ссылке и постановка лайка
                    print('liKe')
                    time.sleep(random.randrange(10)) # сдесь нужна большая пауза чтобы не заподозрили что работает бот примерно 100 секунд

                except Exception as ex:
                    print(ex)



            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

hashtag_search(username, password, 'ковка')
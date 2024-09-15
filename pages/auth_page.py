from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = url if url else 'https://www.saucedemo.com/'
        super().__init__(web_driver, url)

# Указываю локаторы по мере их появления в тестах

    # Авторизация
    name = WebElement(id='user-name')
    password = WebElement(id='password')
    btn_input = WebElement(id='login-button')
    title = WebElement(xpath="//span[@class='title']")
    #name_catalog = WebElement(xpath='//*[@id="header_container"]/div[2]/span[1]')

    # Выбор товара
    product = WebElement(xpath='//*[@id="item_4_title_link"]/div')
    price_product = WebElement(xpath="//div[@class ='inventory_item_price'][1]")
    add_btn = WebElement(id='add-to-cart-sauce-labs-backpack')
    delete_btn = WebElement(id='remove-sauce-labs-backpack')
    icon_cart = WebElement(class_name='shopping_cart_link')

    # Страница корзины
    registration_btn = WebElement(id='checkout')

    # Страница оформления
    #registration_title = WebElement(xpath="//span[@class='title']")
    first_name = WebElement(id='first-name')
    last_name = WebElement(id='last-name')
    postal_code = WebElement(id='postal-code')
    continue_btn = WebElement(id='continue')
    item_total = WebElement(class_name='summary_subtotal_label')
    finish_btn = WebElement(id='finish')

    success_text = WebElement(class_name='complete-header')







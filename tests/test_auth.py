import pytest
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage

@pytest.mark.parametrize('name', ["standard_user"], ids=["positive_name"])
@pytest.mark.parametrize('password', ["secret_sauce"], ids=["positive_password"])
def test_authorisation(driver, name, password):

    # Авторизация в магазине с валидными данными
    page = AuthPage(driver)
    page.name.send_keys(name)
    page.password.send_keys(password)
    page.btn_input.click()
    catalog_title = page.title.get_text()

    # Проверка, что авторизация прошла успешно
    assert page.get_current_url() == "https://www.saucedemo.com/inventory.html", 'Ошибка, URL не совпадают'
    print('\n', "URL корректа")
    assert catalog_title == 'Products', 'Название раздела не совпадает'
    print(catalog_title, '== Products')
    print("Авторизация прошла успешно")

    # Поиск товара по каталогу
    our_product = page.product.get_text()
    assert our_product == "Sauce Labs Backpack", 'Название товара не совпадает'
    print(our_product,  '== Sauce Labs Backpack')
    price = page.price_product.get_text()
    print(price)
    assert page.add_btn.is_clickable() == True, 'Кнопка не кликабельна'
    page.add_btn.click()
    print("Копка кликабельна. Товар добавлен в корзину.")
    assert page.delete_btn.is_presented() == True, 'Кнопка не изменилась'
    print("Кнопка в карточке товара изменила состояние на 'удалить из корзины'")
    assert page.icon_cart.is_clickable() == True, 'Иконка корзины не кликабельна'
    page.icon_cart.click()
    print("Иконка корзин кликабельна. Перешли на страниц корзины.")

    # Сверка товара в корзине, после добавления
    assert page.product.get_text() == our_product, 'Название товара не совпадает'
    print("Название товара совпадает")
    assert page.price_product.get_text() == price, 'Стоимость товара не совпадает'
    print("Стоимость товара совпадает")

    # Оформление покупки
    assert page.registration_btn.is_clickable() == True, 'Кнопка не кликабельна'
    page.registration_btn.click()
    print("Копка кликабельна. Перешли на страницу оформления.")

    # Перешли на страницу оформления покупки
    assert page.get_current_url() == "https://www.saucedemo.com/checkout-step-one.html", 'Ошибка, URL не совпадают'
    print('\n', "URL корректа")
    registration_title = page.title.get_text()
    assert registration_title == 'Checkout: Your Information', 'Название раздела не совпадает'
    print(registration_title, '== Checkout: Your Information')
    print("Перешли на страницу оформления покупки")

    # Вводим сведения о заказчике
    page.first_name.send_keys("Svetlana")
    page.last_name.send_keys("Gray")
    page.postal_code.send_keys("123456")
    assert page.continue_btn.is_clickable() == True, 'Кнопка не кликабельна'
    page.continue_btn.click()
    print("Копка кликабельна. Перешли на страницу завершения оформления покупки.")

    # Страница сверки. Завершение оформления покупки
    assert page.get_current_url() == "https://www.saucedemo.com/checkout-step-two.html", 'Ошибка, URL не совпадают'
    print('\n', "URL корректа")
    registration_overview = page.title.get_text()
    assert registration_overview == 'Checkout: Overview', 'Название раздела не совпадает'
    print(registration_overview, '== Checkout: Overview')
    print("Перешли на страницу завершения оформления покупки.")

    # Сверка товара и стоимости перед оплатой
    assert page.product.get_text() == our_product, 'Название товара не совпадает'
    print("Название товара совпадает")
    assert page.price_product.get_text() == price, 'Стоимость товара не совпадает'
    print("Стоимость товара совпадает")
    assert page.item_total.get_text() == "Item total: " + price
    print("Стоимость общего количества товара совпадает")
    assert page.finish_btn.is_clickable() == True, 'Кнопка не кликабельна'
    page.finish_btn.click()
    print("Копка кликабельна. Перешли на страницу завершения оформления покупки.")

    complete_title = page.title.get_text()
    assert complete_title == 'Checkout: Complete!', 'Название раздела не совпадает'
    print(complete_title, '== Checkout: Complete!')
    finish_text = page.success_text.get_text()
    assert finish_text == 'Thank you for your order!', 'Название раздела не совпадает'
    print(finish_text, '== Thank you for your order!')
    print("Успешное завершение оформления покупки.")














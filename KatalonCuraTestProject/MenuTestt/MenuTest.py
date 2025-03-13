from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from MenuTestt.HomePage import check_home_link


def check_menu(driver):
    menu_toggle = driver.find_element(By.ID, "menu-toggle")
    menu_panel = driver.find_element(By.ID, "sidebar-wrapper")

    is_menu_visible_before = menu_panel.is_displayed()  # Açık mı kontrol et

    # Menü butonuna tıkla
    menu_toggle.click()

    WebDriverWait(driver, 10).until(lambda d: menu_panel.is_displayed() != is_menu_visible_before)

    # Menü açıldı mı kontrol et
    if menu_panel.is_displayed():
        print("OK! Menü açıldı.")
    else:
        print("Hata! Menü açılmadı.")


    check_home_link(driver)

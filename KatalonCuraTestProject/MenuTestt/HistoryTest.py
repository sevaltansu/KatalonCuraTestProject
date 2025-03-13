from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_history_test(driver):
    menu_toggle = driver.find_element(By.ID, "menu-toggle")
    menu_toggle.click()

    history_button =driver.find_element(By.XPATH, "//a[@href='history.php#history']")
    expected_url = "https://katalon-demo-cura.herokuapp.com/history.php#history"
    history_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    current_url = driver.current_url

    # URL doğrulaması
    if current_url == expected_url:
        print("OK! History sayfasına yönlendirildi.")
    else:
        print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")

    history_title= driver.find_element(By.XPATH, "//h2[text()='History']").text

    if "History" in history_title:
        print("OK. History Başlığı alındı")
    else:
        "HATA. Başlık eksik"


    facility = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID,"facility"))
    ).text
    redmission=driver.find_element(By.ID,"hospital_readmission").text
    program = driver.find_element(By.ID, "program").text
    comment = driver.find_element(By.ID,"comment").text
    assert facility == "Hongkong CURA Healthcare Center"
    assert program=="None"
    assert redmission =="Yes"
    assert comment =="demo"

    go_to_homepage_button = driver.find_element(By.XPATH, "//a[@href='https://katalon-demo-cura.herokuapp.com/']")

    expected_url = "https://katalon-demo-cura.herokuapp.com/"
    go_to_homepage_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    current_url = driver.current_url

    # URL doğrulaması
    if current_url == expected_url:
        print("OK! Home Page sayfasına yönlendirildi.")
    else:
        print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")


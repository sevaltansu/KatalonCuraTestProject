from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_profile_test(driver):
    menu_toggle = driver.find_element(By.ID, "menu-toggle")
    menu_toggle.click()

    profile_button =driver.find_element(By.XPATH, "//a[@href='profile.php#profile' and text()='Profile']")
    expected_url = "https://katalon-demo-cura.herokuapp.com/profile.php#profile"
    profile_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    current_url = driver.current_url

    # URL doğrulaması
    if current_url == expected_url:
        print("OK! Profile sayfasına yönlendirildi.")
    else:
        print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")



    profile_heading = driver.find_element(By.XPATH, "//h2[text()='Profile']").text
    assert "Profile"==profile_heading

    logout_button = driver.find_element(By.XPATH, "//a[@href='https://katalon-demo-cura.herokuapp.com/authenticate.php?logout']")

    expected_url = "https://katalon-demo-cura.herokuapp.com/"
    logout_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    current_url = driver.current_url

    # URL doğrulaması
    if current_url == expected_url:
        print("OK! Çıkış Yapıldı.")
    else:
        print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")




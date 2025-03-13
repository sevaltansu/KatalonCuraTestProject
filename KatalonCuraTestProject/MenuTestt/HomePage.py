from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_home_link(driver):
    try:
        home_button = driver.find_element(By.XPATH, "//a[@href='./']")
        expected_url = "https://katalon-demo-cura.herokuapp.com/"
        home_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        current_url = driver.current_url

        # URL doğrulaması
        if current_url == expected_url:
            print("Başarılı! Home sayfasına yönlendirildi.")
        else:
            print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")

    except Exception as e:
        print(f"Home linkine tıklanamadı veya yönlendirme başarısız: {e}")


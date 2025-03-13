from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def check_facebook_icon(driver):
    try:
        fb_link_element = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-facebook')]/parent::a")
        expected_url = fb_link_element.get_attribute("href")

        if not expected_url:
            print("Hata! Facebook ikonunun içinde yönlendirme linki bulunamadı.")
            return
        fb_link_element.click()
        WebDriverWait(driver, 5).until(EC.url_contains("facebook.com"))
        current_url = driver.current_url
        if "facebook.com" in current_url:
            print("OK! Facebook sayfasına yönlendirildi.")
        else:
            print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")
    except Exception as e:
        print(f"Facebook ikonuna tıklanamadı veya yönlendirme başarısız: {e}")

def check_twitter_icon(driver):
    try:
        twitter_link_element = driver.find_element(By.XPATH, "//i[contains(@class, 'fa-twitter')]/parent::a")
        expected_url = twitter_link_element.get_attribute("href")

        if not expected_url:
            print("Hata! Twitter ikonunun içinde yönlendirme linki bulunamadı.")
            return

        twitter_link_element.click()

        WebDriverWait(driver, 5).until(EC.url_contains("twitter.com"))

        current_url = driver.current_url

        if "twitter.com" in current_url:
            print("Başarılı! Twitter sayfasına yönlendirildi.")
        else:
            print(f"Hata! Beklenen: {expected_url}, ancak gidilen: {current_url}")

    except Exception as e:
        print(f"Twitter ikonuna tıklanamadı veya yönlendirme başarısız: {e}")

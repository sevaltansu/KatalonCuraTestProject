from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def logintest(driver):
    # Senaryo 1: Başarısız Giriş (Yanlış Kullanıcı Adı veya şifre)
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "btn-make-appointment").click()
    name = driver.find_element(By.ID, "txt-username")
    name.send_keys("seval")
    passw = driver.find_element(By.ID, "txt-password")
    passw.send_keys("seval")
    loginButton = wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))
    loginButton.click()
    mesaj = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'text-danger')]"))).text

    if "Login failed! Please ensure the username and password are valid." in mesaj:
        print("OK.GİRİŞ YAPILAMADI UYARI VERİLDİ")
    else:
        print("hata")

    driver.find_element(By.ID, "btn-make-appointment").click()
    name = driver.find_element(By.ID, "txt-username")
    name.send_keys("John Doe")
    passw = driver.find_element(By.ID, "txt-password")
    passw.send_keys("ThisIsNotAPassword")
    loginButton = wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))
    loginButton.click()

    try:
        make_appointment_title = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Make Appointment']")))

        # Başlık başarılı bir şekilde bulunduysa
        print("Başarılı giriş yapıldı ve 'Make Appointment' başlığı görünüyor.")

    except:
        # Başlık bulunamadıysa
        print("Hata: Başlık bulunamadı, giriş başarısız olabilir.")








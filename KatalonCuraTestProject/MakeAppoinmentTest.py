#senaryo başlık kontrolü
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def makeappointment(driver):
    wait=WebDriverWait(driver,10)
    #Randevu alma sayfasına giriş kontrolü
    try:
        make_appointment_title = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Make Appointment']")))
        # Başlık başarılı bir şekilde bulunduysa
        print("'Make Appointment' başlığı görünüyor.")

    except:
        # Başlık bulunamadıysa
        print("Hata: Başlık bulunamadı")

    #Hastane seçimi
    facility_dropdown=wait.until(EC.visibility_of_element_located((By.ID, "combo_facility")))
    select=Select(facility_dropdown)
    select.select_by_index(1)


    applybox=driver.find_element(By.ID,"chk_hospotal_readmission")
    applybox.click()
    if applybox.is_selected():
        print("checkbox işaretlendi")


    # İkinci radio butonunu seç
    radio2 = driver.find_element(By.ID, "radio_program_none")
    radio2.click()
    if radio2.is_selected():
        print("Programlardan none işaretlendi")



   # tarih girme
    text_date=driver.find_element(By.ID,"txt_visit_date")
    text_date.send_keys("")
    wait.until(EC.element_to_be_clickable((By.ID, "btn-book-appointment"))).click()
    #eğer boşsa ve giriş yapılmaya çalışırsa hata
    try:
        datepicker = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), '1') and contains(@class, 'day')]"))
        )
        print("OK. TARİH ALINMADAN RANDEVU ALINMADI")

    except:
        print("Hata! Tarih alınmadan randevu alındı")

    text_date.send_keys("16/03/2025")
    print("tarih alındı")

    driver.find_element(By.ID,"txt_comment").send_keys("demo")

    wait.until(EC.element_to_be_clickable((By.ID, "btn-book-appointment"))).click()
    #appointment_confirmation=wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Appointment Confirmation']"))).text
    try:
        appointment_confirmation = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Appointment Confirmation']"))
        ).text
        print("OK. GİRİŞ BAŞARILI,Appointment Confirmation başlığı alındı")
    except Exception:
        print("Hata giriş yapılamadı.")

    facility = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID,"facility"))
    ).text

    #ALINAN RANDEVUNUN DOĞRULUĞU
    redmission=driver.find_element(By.ID,"hospital_readmission").text
    program = driver.find_element(By.ID, "program").text
    visit_date = driver.find_element(By.ID, "visit_date").text
    comment = driver.find_element(By.ID,"comment").text
    assert facility == "Hongkong CURA Healthcare Center"
    assert redmission =="Yes"
    assert visit_date=="16/03/2025"
    assert comment =="demo"







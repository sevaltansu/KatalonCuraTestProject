from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from MakeAppoinmentTest import makeappointment
from MenuTestt.HistoryTest import check_history_test
from MenuTestt.MenuTest import check_menu
from MenuTestt.ProfilePage import check_profile_test

from footer.FooterTest import footer
from loginTest import logintest

optionss=webdriver.ChromeOptions()
service=Service("./chromedriver.exe")
optionss.add_experimental_option(name="detach", value=True)
driver=webdriver.Chrome(service=service,options=optionss)
driver.get("https://katalon-demo-cura.herokuapp.com/")

#menu testi
check_menu(driver)
#giriş testi
logintest(driver)
#randevu kontrolü
makeappointment(driver)
#history sayfası
check_history_test(driver)
#profile
check_profile_test(driver)
footer(driver)

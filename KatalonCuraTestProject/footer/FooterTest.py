from selenium.webdriver.common.by import By

from footer.SocialMediaTest import check_facebook_icon, check_twitter_icon


def footer(driver):

    footer = driver.find_element(By.TAG_NAME, 'footer')

    check_facebook_icon(driver)
    check_twitter_icon(driver)




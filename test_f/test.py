from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://fe-app.stage.nogin.com/log_in")
login_email_field = driver.find_element(By.ID, "login")
login_email_field.send_keys("ogooglechormea@nieise.com")
login_password_field = driver.find_element(By.ID, "password")
login_password_field.send_keys("12345678")
login_button = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div/div/form/div[3]/button")
login_button.click()
sleep(5)
driver.quit()

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    email = input("Enter email: ")
    password = input("Enter password: ")
    driver = webdriver.Chrome("C:/Users/trist/Downloads/chromedriver_win32/chromedriver")
    driver.get("https://strava.com/login")
    login_script(email, password, driver)


def login_script(email, password, driver):
    login_email = driver.find_element(By.ID, 'email')
    login_password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')

    login_email.click()
    login_email.send_keys(email)
    login_password.click()
    login_password.send_keys(password)
    login_button.click()

if __name__ == "__main__":
    main()



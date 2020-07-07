import sys

from scanner import Scanner
from selenium import webdriver

from validator import is_valid_url


def handle_terminal_args(args, driver):
    if len(args) == 2:
        https_address = sys.argv.pop()
        if is_valid_url(https_address):
            driver.get(https_address)
            driver.maximize_window()
        else:
            driver.quit()
            print("please run again with valid url: for example :: 'https://www.google.com'")
            exit()
    else:
        driver.minimize_window()
        valid_address = input("Please input valid url:\n")
        match = is_valid_url(valid_address)
        while not match:
            valid_address = input("Please input valid url: for example 'https://www.google.com'\n")
            match = is_valid_url(valid_address)
        if match:
            driver.maximize_window()
            driver.get(valid_address)


scan = Scanner(webdriver.Chrome("drivers/chromedriver"))
handle_terminal_args(sys.argv, scan.get_driver())

scan.number_of_html_form_elements()
scan.number_of_html_image_tags()

scan.quit_driver()

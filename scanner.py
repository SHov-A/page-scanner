import sys
from validator import is_valid_url


class Scanner:
    def __init__(self, driver):
        self.__driver = driver

    def number_of_html_form_elements(self):
        number_of_html_form_elements = 0
        element_form = self.__driver.find_elements_by_xpath("//form")
        for e in element_form:
            method_attribute = e.get_attribute(name="method")
            if str(method_attribute).lower() != "post":
                number_of_html_form_elements += 1
        print("The number of <form/> tags with 'method=get' is :: %s" % number_of_html_form_elements)

    def number_of_html_image_tags(self):
        element_image = self.__driver.find_elements_by_xpath("//img")
        print("The number of <img/> tags is :: %s" % len(element_image))

    def get_driver(self):
        return self.__driver

    def quit_driver(self):
        self.__driver.quit()

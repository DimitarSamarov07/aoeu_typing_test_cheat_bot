from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://typing-speed-test.aoeu.eu/")

agreement_button = driver.find_element_by_xpath("//button[text()='AGREE']")
agreement_button.click()
input_el = driver.find_element_by_id("input")
span_arr_of_words = driver.find_element_by_id("words").find_elements_by_tag_name("span")

for word in span_arr_of_words:
    input_el.send_keys(word.get_attribute("innerHTML") + " ")
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://typing-speed-test.aoeu.eu/")

agreement_button = driver.find_element_by_xpath("//button[text()='AGREE']")
agreement_button.click()
input_el = driver.find_element_by_id("input")
span_arr_of_words = driver.find_element_by_id("words").find_elements_by_tag_name("span")

# Get the texts before the actual typing test so it's faster
plain_words_arr = []
for word in span_arr_of_words:
    plain_words_arr.append(word.get_attribute("innerHTML") + " ")

for index, word in enumerate(span_arr_of_words):
    input_el.send_keys(plain_words_arr[index])

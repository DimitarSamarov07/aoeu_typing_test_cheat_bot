from selenium import webdriver

# Initialize the driver and get the page
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://typing-speed-test.aoeu.eu/")

try:
    agreement_button = driver.find_element_by_xpath("//button[text()='AGREE']")
    agreement_button.click()

except NoSuchElementException:
    print("No agreement button was found. If this is a bug, report it.\n"
          "For now if there's a button, you can click it yourself")

input_el = driver.find_element_by_id("input")
span_arr_of_words = driver.find_element_by_id("words").find_elements_by_tag_name("span")

# Get the texts before the actual typing test so it's faster
plain_words_arr = []
for word in span_arr_of_words:
    plain_words_arr.append(word.get_attribute("innerHTML") + " ")

input_el.send_keys(" ".join(plain_words_arr))

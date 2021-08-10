from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Initialize the driver and get the page
driver = webdriver.Firefox()
driver.get("https://typing-speed-test.aoeu.eu/")

# If the button is found click it
try:
    agreement_button = driver.find_element_by_xpath("//button[text()='AGREE']")
    agreement_button.click()

# If not, just assume that it doesn't exist or that the user
# has already clicked on it
except NoSuchElementException:
    print("No agreement button was found. If this is a bug, report it.\n"
          "For now if there's a button, you can click it yourself")

# Get the input element
input_el = driver.find_element_by_id("input")

# Get all the spans containing the actual words
span_arr_of_words = driver.find_element_by_id("words").find_elements_by_tag_name("span")

# Get the texts before the actual typing test so it's faster
plain_words_arr = []
for word in span_arr_of_words:
    plain_words_arr.append(word.get_attribute("innerHTML") + " ")

# Send one big string with the words divided by a space
# (this should in theory be the highest speed you can achieve)
input_el.send_keys(" ".join(plain_words_arr))

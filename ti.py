from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

# Launch the web browser using the Chrome webdriver
# driver = webdriver.Chrome()

# # Set the path to the Firefox driver executable
# firefox_driver_path = '/home/venkatesh/Desktop/Learning/selenium/Drivers/geckodriver'

# # Create a Firefox driver instance
# driver = webdriver.Firefox(executable_path=firefox_driver_path)

# driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")


# firefox_binary_path = '/snap/bin/firefox'
# options = FirefoxOptions()
# options.binary_location = firefox_binary_path
# # driver = Firefox(options=options)


# # Create a Firefox service instance
# firefox_service = webdriver.firefox.service.Service(executable_path=GeckoDriverManager().install(),options=options)

# # Create a Firefox driver instance using the service
# driver = webdriver.Firefox(service=firefox_service)


# Navigate to the appropriate page
driver.get("https://portal.icaniotech.com/")
# Add cookies
# cookies = [
#     {'name': 'stk', 'value': '64fe4dcedd06fd4f9f374572c3274322'},
#     {'name': 'f153d1cace', 'value': '974eda90eefec6ffbd48834efc07a101'},
#     {'name': 'CSRF_TOKEN', 'value': 'ffd69c818335658e271820dbd3e1182868f6cfe6f68536a0aa932e18a895f0572d8c3d33fdff413275495430df847606c77cca580e762dcd446c27322d2c7345'},
#     {'name': '_zcsr_tmp', 'value': 'ffd69c818335658e271820dbd3e1182868f6cfe6f68536a0aa932e18a895f0572d8c3d33fdff413275495430df847606c77cca580e762dcd446c27322d2c7345'},
#     {'name': '9ca8afda3c', 'value': '7dabc7af8f9ee72b83436b6d3f7a868b'},
#     {'name': 'CT_CSRF_TOKEN', 'value': 'ffd69c818335658e271820dbd3e1182868f6cfe6f68536a0aa932e18a895f0572d8c3d33fdff413275495430df847606c77cca580e762dcd446c27322d2c7345'},
#     {'name': 'com_chat_owner', 'value': '1680591727285'},
#     {'name': 'com_avcliq_owner', 'value': '1680591727286'},
#     {'name': '814af6c8e8', 'value': '507b8f9aa85183d18f90c8d5004fe90f'},
#     {'name': 'bc5826c95a', 'value': 'c4f2ab33f666f65ab855f401e6f2a508'}
# ]

# for cookie in cookies:
#     driver.add_cookie(cookie)

# driver.execute_script("localStorage.setItem(`60010696772_frequent_smileys`, `{'work':[':smile:',':happy:',':joy:',':love:',':thinking:',':surprise:',':thumbsup:',':thumbsdown:',':namaste:',':tensed:',':biceps:',':doubt:',':super:',':clap:',':fireworks:',':food:',':gift-box:'],'emoji':[':grinning:',':blush:',':wink:',':stuck-out-tongue-winking-eye:',':flushed:',':sob:',':sweat-smile:',':scream:',':sunglasses:',':raised-hands:',':wave:',':house-with-garden:',':point-up-2:',':dancer:',':bouquet:',':round-pushpin:',':heavy-plus-sign:'],'animated':[':smile!:',':happy!:',':joy!:',':love!:',':thinking!:',':surprise!:',':thumbsup!:',':thumbsdown!:',':namaste!:',':tensed!:',':biceps!:',':doubt!:',':super!:',':clap!:',':fireworks!:',':food!:',':gift-box!:'],'customemoji':[],'sticker':[]}`);")
# driver.execute_script("localStorage.setItem('micsTabSwitchTim', '1680591726349');")

# driver.execute_script("localStorage.setItem('micsnotificationtime66', '1680591726349');")

# driver.execute_script("localStorage.setItem('wms_firstloaded', '1680591729238');")
sign_in_button = driver.find_elements(
    By.XPATH,
    "//*[@id=`_google_GoogleLoginPortlet_INSTANCE_pdls_openidconnectform`]/button",
)
sign_in_button[0].click()
# refresh the page
# driver.refresh()

time.sleep(1)

google_button = driver.find_elements(
    By.XPATH, "//*[@id='signin_div']/div[5]/span[1]/div/span[2]"
)
google_button[0].click()

time.sleep(1)

input = driver.find_elements(By.ID, "identifierId")
print(input)
input[0].send_keys("venkatesh.b@icanio.com")

time.sleep(1)

next_button = driver.find_elements(By.XPATH, "//*[@id='identifierNext']/div/button")
next_button[0].click()
time.sleep(1)
input = driver.find_elements(By.NAME, "password")
input[0].send_keys("Password")
next2_button = driver.find_elements(By.XPATH, "//*[@id='passwordNext']/div/button")
next2_button[0].click()

time.sleep(20)


# checkOut=driver.find_elements(By.ID,"ZPD_Top_Att_Stat")
# if "Check-out" in checkOut[0].text:
#     print("Checkout Successfully")
# else:
#     print("Check in successfully")

# checkOut[0].click()
# # time.sleep(1)

time.sleep(30)
# driver.implicitly_wait(1000000)  # set timeout to 10 seconds

# Fill in the check-in form
# username = driver.find_element_by_name("username")
# username.send_keys("your_username")
# password = driver.find_element_by_name("password")
# password.send_keys("your_password")
# submit_button = driver.find_element_by_xpath("//input[@type='submit']")
# submit_button.click()

# Wait for the file to be checked in
driver.implicitly_wait(10)

driver.quit()


# By.ID: Finds elements based on their id attribute value.
# By.CLASS_NAME: Finds elements based on their class attribute value.
# By.XPATH: Finds elements based on an XPath expression.
# By.NAME: Finds elements based on their name attribute value.
# By.TAG_NAME: Finds elements based on their HTML tag name.
# By.LINK_TEXT: Finds a elements based on their exact link text.
# By.PARTIAL_LINK_TEXT: Finds a elements based on their partial link text.

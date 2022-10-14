from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from HOP_functions import *


# command to run all the tests: python -m pytest

def test_page_title() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")
      
    title = "Hartlink Online Portal"
    actual_title = driver.title
    driver.quit()
    assert title == actual_title

def test_header_elements() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")

    header_elements_list= driver.find_elements(By.ID, 'staticBannerMenu')
    for header_element in header_elements_list:
        actual_header_elements = header_element.text

    driver.quit()
    expected_welcome_text = '''A A A
Contact Us
Home
Login
Register'''
    assert expected_welcome_text == actual_header_elements

def test_menu_elements() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")
    open_menu(driver)

    menu_elements_list= driver.find_elements(By.XPATH, '//*[@id="globalTopMenu"]/div')
    for menu_element in menu_elements_list:
        actual_menu_elements = menu_element.text

    driver.quit()
    expected_menu_elements = '''Reminders
Login Name Reminder
Reset Password
Reset PIN
Apply To Join The Scheme
Application Options
Scheme Communications
Pensions Compass
Scheme Information
Investments
Investment Options
General Information
Contact Us
Useful Websites
Useful Terms
My Documents
My Documents'''
    assert expected_menu_elements == actual_menu_elements
    
def test_welcome_text() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")

    homepage_wording_list = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/main/div[1]')
    for homepage_wording_element in homepage_wording_list:
        actual_welcome_text = homepage_wording_element.text

    driver.quit()
    expected_welcome_text = '''Welcome
to the Pfizer Pension Arrangements.'''
    assert expected_welcome_text == actual_welcome_text

def test_footer() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")

    footer_elements_list = driver.find_elements(By.CLASS_NAME, 'hop-footer-wrapper')
    for footer_element in footer_elements_list:
        actual_footer_elements = footer_element.text

    driver.quit()
    expected_footer_elements = '''Capita plc Capita
Accessibility Privacy & Cookie Policy FAQ Terms & Conditions
Capita Pension Solutions is a trading name of Capita Pension Solutions Limited and Capita Employee Benefits (Consulting) Limited. Part of Capita plc. www.capita.com. Capita Pension Solutions Limited and Capita Employee Benefits (Consulting) Limited are registered in England & Wales No: 02260524 and 01860772 respectively. Registered Office: 65 Gresham Street, London, EC2V 7NQ. Separately authorised and regulated by the Financial Conduct Authority'''
    assert expected_footer_elements == actual_footer_elements
       
def test_contact_us_wording() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")
    open_contact_us_scheme(driver)

    contact_us_wording_list = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
    for contact_us_wording_element in contact_us_wording_list:
        actual_contact_us_wording = contact_us_wording_element.text

    driver.quit()

    expected_contact_us_wording = '''Contact Us
If you would like to contact us for any further information, click the Contact Us button below:
To notify us of the death of a pension scheme member, please click the Bereavement Form button below:
Bereavement Form
Alternatively you can write to us at:
Pfizer Pension Arrangements
Capita Pension Solutions Ltd
PO Box 555
Stead House
Darlington
DL1 9YT
United Kingdom
Or telephone us on: 0800 328 4233
Or email us at: pfizerpensions@capita.co.uk
Please quote your National Insurance Number in any correspondence.
Our aim is to deliver the highest possible standards of service to our customers. If you are dissatisfied with any aspect of the service that you have received from the Scheme please get in touch using the contact details above.'''
    assert expected_contact_us_wording == actual_contact_us_wording

def test_login_wording() -> None:
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    open_url(options, driver, "https://qaportal.hartlinkonline.co.uk/pfizer")
    open_login_header(driver)

    login_wording_list = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
    for login_wording_element in login_wording_list:
        actual_login_wording = login_wording_element.text

    driver.quit()

    expected_login_wording = '''1
Login Name
2
Password & PIN
3
Confirmation
Login Name
Your Login Name
In order to ensure your queries are directed to the correct team, please login to your retirement account where a range of options will be available to you.'''
    assert expected_login_wording == actual_login_wording 
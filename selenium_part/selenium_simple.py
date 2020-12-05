import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_videos_today_about_cats(driver):
    url = "https://www.youtube.com/results?search_query=cats"
    driver.get(url)
    time.sleep(4)
    filter_button = driver.find_element_by_xpath('//yt-icon[@class="style-scope ytd-toggle-button-renderer"]')
    driver.execute_script("arguments[0].click();", filter_button)
    time.sleep(4)
    today_button = driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-search-filter-renderer"]')
    driver.execute_script("arguments[0].click();", today_button)
    time.sleep(4)
    print('searching for cat videos uploaded today')
    wait = WebDriverWait(driver, 10)
    visible = EC.visibility_of_element_located
    wait.until(visible((By.ID, "video-title")))
    list_sites = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
    for index, site in enumerate(list_sites):
        relevant_text = site.get_attribute('aria-label')
        logging.info(''.join(['index: ', str(index), '\nvideo information: ', relevant_text]))
        print('iterating index: ', index)
    print('finished logging cat videos to debug.log')    
    

def print_wanted_elements(elements):
    wanted_elements = ['Table Tennis', 'Badminton', 'Cricket', 'Volley ball']
    for element in elements:
        text = element.text
        if text in wanted_elements:
            print(text)

def practise_tables(driver):
    url = "https://sqengineer.com/practice-sites/practice-tables-selenium/"
    driver.get(url)
    time.sleep(3)
    elements = driver.find_elements_by_xpath('//table[@id="table1"]/tbody/tr/td/a')
    for element in elements:
        url = element.get_attribute('href')
        #element.click()
        print(url)
    elements = driver.find_elements_by_xpath('//table[@id="table2"]/tbody/tr/td')
    print_wanted_elements(elements)
    print('\n\n\n')

def fill_out_form(driver):
    url = "https://sqengineer.com/practice-sites/basic-web-elements/"
    driver.get(url)
    time.sleep(3)

    input_name = driver.find_element_by_xpath('//input[@name="fname"]')
    input_name.send_keys('generic name')

    input_name = driver.find_element_by_xpath('//input[@name="lname"]')
    input_name.send_keys('generic name')

    input_gender = driver.find_element_by_xpath('//input[@value="male"]')
    input_gender.click()

    input_email = driver.find_element_by_xpath('//input[@name="emailID"]')
    input_name.send_keys('generic email name')

    driver.find_element_by_xpath('//select[@id="selectBox"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//option[@value="LA"]').click()
    time.sleep(1)

    #print text
    message = driver.find_element_by_xpath('//label[@id="readText"]').text
    print(message)

    driver.find_element_by_xpath('//input[@type="submit"]').click()
    time.sleep(1)
    form_text = driver.find_element_by_xpath('//div[@class="entry-content"]').text
    print('form_text: ', form_text, '\n\n\n')


def get_youtube_results(driver):
    url = "https://www.youtube.com/results?search_query=Python"
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    time.sleep(5)
    print('loaded url, fetching youtube query: python') 
    visible = EC.visibility_of_element_located
    wait.until(visible((By.ID, "video-title")))
    list_sites = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "video-title")))
    for site in list_sites:
        url = site.get_attribute('href')
        title = site.text
        print('title: ', title, ' url: ', url)
    print('\n\n\n')

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )
    options = Options()
    options.headless = True
    remoteGeckoPath = "/usr/bin/geckodriver"
    print('init driver')
    try: 
        driver = webdriver.Firefox(executable_path=remoteGeckoPath,options=options)
        get_youtube_results(driver)
        fill_out_form(driver)
        practise_tables(driver)
        find_videos_today_about_cats(driver)
    finally:
        driver.quit()
    
if __name__ == "__main__":
    main()

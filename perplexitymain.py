from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import json
def ask(input_text: str, path: str):
    # create webdriver object
    options = Options()
    options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options,executable_path=path)
    

    driver.get("https://www.perplexity.ai/")
    # get element
    element = driver.find_element(By.ID, "ppl-query-input")
    element.send_keys(input_text)
    element.send_keys(Keys.ENTER)
    listofzero=[]
    while True:
        list = []
        log_entries = driver.get_log("performance")
        for entry in log_entries:
            obj_serialized: str = entry.get("message")
            obj = json.loads(obj_serialized)
            message = obj.get("message").get("params").get("type")
            if(str(message) == "Fetch"):
                list.append(message)
        if len(list) == 0:
            listofzero.append("0")
            time.sleep(0.5)
        else:
            time.sleep(0.5)
        if len(listofzero) >= 3:
            time.sleep(1)
            break
    finlist = []
    finlist.append(driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]').text)
    for i in driver.find_element(By.XPATH,"//div[@class='min-h-[81px]'][1]").find_elements(By.XPATH,".//a"):
        finlist.append(f"{i.text}: {i.get_attribute('href')}")
    return finlist
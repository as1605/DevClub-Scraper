from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

rnd=sys.argv[1].upper()

PATH = "C:\\selenium\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://codechef.com/"+rnd)

urls=[]

for problem in driver.find_elements_by_class_name("cc-problem-name"):
	print(problem)
	urls.append(problem.find_element_by_tag_name('div').find_element_by_tag_name('span').find_element_by_tag_name('a').get_attribute('href'))

for url in urls:
	driver.get(url)
	path=rnd+'/'+url.split('/')[-1]
	try:
		os.makedirs(path)
	except:
		pass
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "problem-statement")))
	driver.find_element_by_id("problem-statement").screenshot(path+"/problem.png")
	for test in driver.find_elements_by_tag_name("pre"):
		print(test)
		print(path+'/'+test.find_element_by_xpath("preceding-sibling::h3[1]").get_attribute('id')[:42]+'.txt')
		print(test.find_element_by_tag_name("code").get_attribute("innerText"))
		open(path+'/'+test.find_element_by_xpath("preceding-sibling::h3[1]").get_attribute('id')[:42]+'.txt','w').write(test.find_element_by_tag_name("code").get_attribute("innerText"))

driver.quit()
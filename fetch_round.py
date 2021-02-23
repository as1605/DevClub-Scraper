from selenium import webdriver
import sys
import os

rnd=sys.argv[1]

PATH = "C:\\selenium\\geckodriver.exe"
driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://codeforces.com/contest/"+rnd)

n=int(driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[6]/table/tbody').get_attribute('childElementCount'))-1

urls=[]
for i in range(2,n+2):
	urls.append(driver.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[6]/table/tbody/tr['+str(i)+']/td/a').get_attribute('href'))

for url in urls:
	driver.get(url)
	path=rnd+'/'+url.split('/')[-1]
	try:
		os.makedirs(path)
	except:
		pass
	driver.find_element_by_class_name("problem-statement").screenshot(path+"/problem.png")
	count=int(int(driver.find_element_by_class_name('sample-test').get_attribute('childElementCount'))/2)
	for i in range(1,count+1):
		open(path+'/input'+str(i)+'.txt','w').write(driver.find_element_by_xpath('//*[@id="pageContent"]/div[3]/div[2]/div/div[5]/div[2]/div['+str(i+i-1)+']/pre').get_attribute('innerText'))
		open(path+'/output'+str(i)+'.txt','w').write(driver.find_element_by_xpath('//*[@id="pageContent"]/div[3]/div[2]/div/div[5]/div[2]/div['+str(i+i)+']/pre').get_attribute('innerText'))
driver.quit()
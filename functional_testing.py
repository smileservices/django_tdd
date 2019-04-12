from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
driver.get('http://127.0.0.1:8000')

assert 'Django' in driver.title

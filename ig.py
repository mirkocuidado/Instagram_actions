from selenium import webdriver
from time import sleep
from secret import pas

class InstaBot:

	def __init__(self,username,pas):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		self.username = username

		sleep(1)

		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/p/a").click()
		sleep(2)
		
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pas)

		sleep(2)
		
		self.driver.find_element_by_xpath('//button[@type="submit"]').click()
		
		sleep(5)
		
		self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		
		sleep(2)
		
		n = ['ducatt1', 'djajica']
		self.like_sb(n)

	def like_myself(self):
		self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a").click()
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div/div[1]/a/div").click()
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]").click()
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[4]/div[3]").click()
		sleep(2)

	def like_sb(self, name):
		for i in name:
			
			self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]").click()
			
			sleep(2)
			
			self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(i)
			
			sleep(5)
			
			self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
			
			sleep(2)
			
			self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div").click()
			
			sleep(2)
			
			self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]").click()
			
			sleep(2)
			
			self.driver.find_element_by_xpath("/html/body/div[4]/div[3]").click()
			
			sleep(3)
			
			self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div[2]").click()
			
			sleep(3)

InstaBot('mirko.krajcer',pas)
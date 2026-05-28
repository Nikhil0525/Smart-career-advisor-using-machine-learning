from selenium import webdriver
import unittest
import HtmlTestRunner
import time

class CareerAssist(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
		cls.driver.implicitly_wait(10)
		cls.driver.maximize_window()

	def test_a(self):
		print("Page 1 Completed")
		self.driver.get("http://127.0.0.1:5000/")
		self.driver.find_element_by_name("full_name").send_keys("Julie")
		time.sleep(2)
		self.driver.find_element_by_name("register").click()
		time.sleep(2)
		
	def test_b(self):		
		self.driver.get("http://127.0.0.1:5000/")
		self.driver.find_element_by_name("register").click()
		time.sleep(3)
		print("Page 1 Error: The name is the required field")
		time.sleep(3)
		raise ValueError
	
	def test_c(self):		
		self.driver.get("http://127.0.0.1:5000/form1")
		
		self.driver.find_element_by_name("pos").send_keys("89")
		time.sleep(1)
		self.driver.find_element_by_name("pa").send_keys("100")
		time.sleep(1)
		self.driver.find_element_by_name("pse").send_keys("45")
		time.sleep(1)
		self.driver.find_element_by_name("pcn").send_keys("78")
		time.sleep(1)
		self.driver.find_element_by_name("pe").send_keys("97")
		time.sleep(1)
		self.driver.find_element_by_name("pcoa").send_keys("39")
		time.sleep(1)
		self.driver.find_element_by_name("pm").send_keys("89")
		time.sleep(1)
		
		self.driver.find_element_by_name("hack").send_keys("4")
		time.sleep(1)
		self.driver.find_element_by_name("coding").send_keys("8")
		time.sleep(1)
		
		window_name=self.driver.window_handles[0]
		time.sleep(1)
		self.driver.find_element_by_name("ct").click()
		time.sleep(10)
		self.driver.switch_to_window(window_name)
		time.sleep(2)
		
		self.driver.find_element_by_name("extra").send_keys("yes")
		time.sleep(1)
		self.driver.find_element_by_name("wc1").send_keys("app development")
		time.sleep(1)
		self.driver.find_element_by_name("wc2").send_keys("testing")
		time.sleep(1)
		self.driver.find_element_by_name("is1").send_keys("Data engineering")
		time.sleep(2)
		
		self.driver.find_element_by_name("comm").send_keys("7")
		time.sleep(1)
		self.driver.find_element_by_name("speak").send_keys("7")
		time.sleep(1)
		self.driver.find_element_by_name("mem").send_keys("excellent")
		time.sleep(1)
		
		window_name=self.driver.window_handles[0]
		time.sleep(1)
		self.driver.find_element_by_name("mt").click()
		time.sleep(15)
		self.driver.switch_to_window(window_name)
		time.sleep(2)
		
		self.driver.find_element_by_name("logical").send_keys("8")
		time.sleep(1)
		
		window_name=self.driver.window_handles[0]
		time.sleep(1)
		self.driver.find_element_by_name("lt").click()
		time.sleep(10)
		self.driver.switch_to_window(window_name)
		time.sleep(2)
		
		self.driver.find_element_by_name("rw").send_keys("medium")
		time.sleep(1)
		
		window_name=self.driver.window_handles[0]
		time.sleep(1)
		self.driver.find_element_by_name("rt").click()
		time.sleep(15)
		self.driver.switch_to_window(window_name)
		time.sleep(2)
		
		window_name=self.driver.window_handles[0]
		time.sleep(1)
		self.driver.find_element_by_name("wt").click()
		time.sleep(15)
		self.driver.switch_to_window(window_name)
		time.sleep(2)
		
		self.driver.find_element_by_name("team").send_keys("yes")
		time.sleep(1)
		self.driver.find_element_by_name("ie").send_keys("yes")
		time.sleep(1)
		
		self.driver.find_element_by_name("screen").send_keys("yes")
		time.sleep(1)
		self.driver.find_element_by_name("job").send_keys("job")
		time.sleep(1)
		self.driver.find_element_by_name("comp").send_keys("Product based")
		time.sleep(1)
		self.driver.find_element_by_name("ica").send_keys("testing")
		time.sleep(1)
		self.driver.find_element_by_name("learn").send_keys("no")
		time.sleep(1)
		self.driver.find_element_by_name("hrs").send_keys("4")
		time.sleep(1)
		self.driver.find_element_by_name("mt").send_keys("Technical")
		time.sleep(2)
		
		self.driver.find_element_by_name("register").click()
		time.sleep(3)
		print("Form submitted successfully and all pages working")
		time.sleep(3)
		
	def test_d(self):		
		self.driver.get("http://127.0.0.1:5000/form1")
		
		self.driver.find_element_by_name("pos").send_keys("ret")
		time.sleep(2)
		
		
		self.driver.find_element_by_name("register").click()
		time.sleep(3)
		print("Don't put text in numeric fields and fill all the necessary info")
		time.sleep(2)
		raise ValueError
		

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()
		print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/manali/Desktop/BE/LP2 project/full/assets',report_title="CareerAssist Testing Results"))
    

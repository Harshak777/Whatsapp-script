from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the user or grp: ')
msg = input('Enter your message: ')
count = int(input('Enter how many times u want to text this msg to him'))

input('Press enter after scanning the QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
	msg_box.send_keys(msg)
	but = driver.find_element_by_class_name('_3M-N-')
	but.click()
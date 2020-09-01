from selenium import webdriver
from time import sleep
from creds import username, password

class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        sleep(3)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(3)
    
    def get_lists(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href, 'following')]").click()
        following = self.get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, 'followers')]").click()
        followers = self.get_names()
        nfb = [user for user in following if user not in followers]
        print (nfb)

    def get_names(self):
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        prev_height, height = 0, 1
        while prev_height != height:
            prev_height = height
            sleep(1)
            height = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight)
                return arguments[0].scrollHeight
            """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != ""]
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names
    
my_bot = Instabot(username, password)
try:
    my_bot.get_lists()
    my_bot.driver.close()
except:
    my_bot.driver.close()





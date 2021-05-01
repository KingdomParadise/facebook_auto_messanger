from selenium import webdriver
import time,os,uuid,json,re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import sched, time, timeit
import random
import getpass
from api import SERVER_MESSAGE
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')

LOGIN_TYPE = int(input("Press 1 HUMAN login and 0 for AUTO-MATED login: "))
if LOGIN_TYPE == 1:
    TARGET_PROFILE_ID = input("Enter Profile ID of receiver: ") 
    driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'),chrome_options=chrome_options)
    print("Loading facebook.com ...")
    driver.get('https://web.facebook.com/')
    time.sleep(120)

else:
    EMAILID = input("Enter your Email ID: ")
    PASSWORD = getpass.getpass('Password:')
    TARGET_PROFILE_ID = input("Enter Profile ID of receiver: ")
    driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'),chrome_options=chrome_options)
    print("Loading facebook.com ...")
    driver.get('https://web.facebook.com/')
    time.sleep(5)
    print("Starting Logging in Procees ...")
    driver.find_element_by_id('email').send_keys(EMAILID)
    driver.find_element_by_id('pass').send_keys(PASSWORD)
    time.sleep(3)
    driver.find_element_by_name('login').click()
    print("Logging in ...")
    time.sleep(15)

print("Opening Messenger ...")
driver.get('https://web.facebook.com/messages/t/{}'.format(TARGET_PROFILE_ID))
print("Messenger Loaded ... ")
time.sleep(20)

# INITILIZATION OF CHAT BY BOT
print("INITILIZATION OF CHAT BY BOT")
time.sleep(2)
textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
textAreaElem.send_keys("Hello ...")
time.sleep(2)
sender = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
sender.click()


total_received_messages = 0
loop_counter=0


def CHATTER():
    global total_received_messages
    global loop_counter
    loop_counter=loop_counter+1
    print("_______________________________________")
    print("_______________________________________")
    print("Loop__Counter__", loop_counter)
    
    time.sleep(5)
    
    print("Grabbing Chat Container ...") 
    chat_container = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]')
    chats=chat_container.get_attribute('innerHTML')

    me ="ljqsnud1"
    friend="oo9gr5id"
    # we have to read friend mesage
    print("Making soup ....")
    soup = BeautifulSoup(chats, 'lxml') 
    received_messages = soup.select('div.oo9gr5id')
    print("Comparing the Results ...")
    print("Comaprison Result "+str(total_received_messages)+"_____"+str(len(received_messages))) 
    if total_received_messages<len(received_messages):
        
        # INITILIZATION OF CHAT BY BOT
        print("Sending new mesage ... ")
        
        [x for x in json.loads(SERVER_MESSAGE("123","hello"))] 
        
        DATA_RECEIVED = json.loads(SERVER_MESSAGE("123",str(received_messages[-1].text)))
        total_received_messages=len(received_messages)
        time.sleep(2)
        textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
        def deEmojify(text):
            regrex_pattern = re.compile(pattern = "["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                "]+", flags = re.UNICODE)
            return regrex_pattern.sub(r'',text)
        DATA_RECEIVED = deEmojify(DATA_RECEIVED
                                  )  
        textAreaElem.send_keys(str(DATA_RECEIVED))
        time.sleep(2)
        sender = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
        sender.click()
        print ("Loop again Started ... new message", )
        CHATTER()
    time.sleep(2) 
    CHATTER()      
        
CHATTER()




# 100055137043960 
# 100065878639306
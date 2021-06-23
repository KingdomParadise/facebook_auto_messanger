from selenium import webdriver
import time,os,uuid,json,re,sched, timeit
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import random,time,getpass,csv
from api import SERVER_MESSAGE

def ContactFetcher(driver,your_id,minimum_contacts):
    target_index_seeker = 0
    IDLIST = [] 
    # LOGIN_TYPE = 0 
    
    # EMAILID = input("Enter your Email ID: ") 
    # PASSWORD = getpass.getpass('Password:') 

    # your_id=int(input("Your facebook messenger id  = "))
    # minimum_contacts=int(input("Minimum Contacts to be fetched = "))


    # driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'),options=chrome_options)
    # print("Loading facebook.com ...")
    # driver.get('https://web.facebook.com/')
    # time.sleep(5)
    # print("Starting Logging in Procees ...")

    # driver.find_element_by_id('email').send_keys(EMAILID)
    # driver.find_element_by_id('pass').send_keys(PASSWORD)
    # time.sleep(3)
    # driver.find_element_by_name('login').click()
    # print("Logging in ...")
    # time.sleep(15)


    
    print("Opening Messenger ...")
    driver.get('https://web.facebook.com/messages/t/{}?_rdc=1&_rdr'.format(your_id))
    time.sleep(10)
    print("Messenger Loaded ... ")
    grid=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div")
    # grid.find_elements_by_tag_name('div')[target_index_seeker].click()


# /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[2]


    grid = grid.find_elements_by_tag_name('div')
    for index in range(1,100):
        try:
            try:
                targetchip = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[{index}]")
            except IndexError:break
            chipinnerHTML = targetchip.get_attribute("innerHTML").lower()
            chipinnerHTML = BeautifulSoup(chipinnerHTML,'lxml').text.lower()
            if 'marketplace' in chipinnerHTML or 'market place' in chipinnerHTML:
                print("--> Market Place FOUND ")
                targetchip.click()
                time.sleep(3)
                print("-"*100)
                break
            
            else:print("** NOT MarketPlace CHIP")
        except IndexError:break
     

    print("** clicked")
    time.sleep(10)



    tracker=[]
    def contact_saver(data):
        print("____ writing contact text file")
        with open("fresh_fetched_contacts.txt", "w") as file:
            if len(data)==0:
                pass
            else:
                file.seek(0)  # sets  point at the beginning of the file
                file.truncate()
                for index,x in enumerate(list(set(data))):
                    if index<minimum_contacts:
                        file.write(str(x)+"\n")
        




    while True: 
        try:
            target_html = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")
            # target_html = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]")
            
            soup = BeautifulSoup(target_html.get_attribute("innerHTML"), 'lxml')
            soup = soup.select('div.l9j0dhe7')
            soup = [x.select('a.oajrlxb2.gs1a9yip.g5ia77u1') for x in soup]
            soup = [x for x in soup if x!=[]]
            soup=[str(x[0]['href']).split('/')[-2] for x in soup]
            print(((soup)))
            print(len((soup)))
            tracker.append(len(soup))
            
            
            if len(soup)>=int(minimum_contacts):
                print("==> Criteria achieved.")
                contact_saver(soup)
                return IDLIST
                
            
            # if len(tracker)>=10:
            #     if tracker[-13]==tracker[-12]==tracker[-11]==tracker[-10]==tracker[-9]==tracker[-8]==tracker[-7]== tracker[-6]== tracker[-5]== tracker[-4]==tracker[-3]==tracker[-2]==tracker[-1]:
            #         print("*** SAME")
            #         contact_saver(soup)
            #         return IDLIST 
            
            
            
            
            time.sleep(4)
            moving_bars =driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]")

            # print(len(moving_bars.find_elements_by_tag_name('div')))

            felem = moving_bars.find_elements_by_tag_name('div')[0]
            lelem = moving_bars.find_elements_by_tag_name('div')[-1]

            

            time.sleep(3)
            print("=> moving to last bar")
            lelem.location_once_scrolled_into_view
            # time.sleep(6)
            # felem.location_once_scrolled_into_view

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_lineno)
            continue




# target_html = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")
# soup = BeautifulSoup(target_html.get_attribute("innerHTML"), 'lxml')
# print(len(str(soup)))

# grid=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div")

# soup = BeautifulSoup(grid.get_attribute("innerHTML"), 'lxml')
# print(len(str(soup)))


# time.sleep(5)

 
# grid2=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")
 
# grid2.element.location_once_scrolled_into_view




# grid2 = grid2.get_attribute("innerHTML")
# soup = BeautifulSoup(grid2, 'lxml')

# print(soup)

# ids = [x.select('a')[0]['href'] for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# soup = [x.select('a')[0].select('span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5')[0].text.replace('\n','').strip() for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# names = [re.sub(' +', ' ',x) for x in soup]
# dictionary = dict(zip(names, ids))
# print(dictionary)
# print(len(ids))




        
# file=''
# file = open('tes.html', 'r').read()
# soup = BeautifulSoup(file, 'lxml')
# ids = [x.select('a')[0]['href'].replace('/messages/t/','')[:-1] for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# soup = [x.select('a')[0].select('span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5')[0].text.replace('\n','').strip() for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# names = [re.sub(' +', ' ',x) for x in soup]
# dictionary = dict(zip(names, ids))
# [print(x, "__________" ,dictionary[x]) for x in dictionary]
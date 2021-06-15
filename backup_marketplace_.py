# from selenium import webdriver
# import time,os,uuid,json,re,sched, timeit
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# import random,time,getpass,csv
# from api import SERVER_MESSAGE

# IDLIST = []

# with open('contact_ids.csv', 'r') as file:
#     reader = csv.reader(file)
#     for index, row in enumerate(reader):
#         if index>0:
#             IDLIST.append(row[0])
            





# MESSAGES_LOG=[ {"id":x,"sessional_len":0,"init_messgae_handler":0} for x in IDLIST]
# chrome_options = Options()
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('log-level=3')

# LOGIN_TYPE = 0
# # LOGIN_TYPE = int(input("Press 1 HUMAN login and 0 for AUTO-MATED login: "))

# if LOGIN_TYPE == 1:
#     driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'),options=chrome_options)
#     print("Loading facebook.com ...")
#     driver.get('https://web.facebook.com/')
#     time.sleep(20)

# else:
    
#     EMAILID = "mashoodurrehmanofficial@gmail.com"
#     PASSWORD = "play@715"
  
#     # EMAILID = input("Enter your Email ID: ") 
#     # PASSWORD = getpass.getpass('Password:') 
#     minimum_contacts=int(input("Minimum Contacts to be fetched = "))
    
    
#     driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),'chromedriver.exe'),options=chrome_options)
#     print("Loading facebook.com ...")
#     driver.get('https://web.facebook.com/')
#     time.sleep(5)
#     print("Starting Logging in Procees ...")
    
#     driver.find_element_by_id('email').send_keys(EMAILID)
#     driver.find_element_by_id('pass').send_keys(PASSWORD)
#     time.sleep(3)
#     driver.find_element_by_name('login').click()
#     print("Logging in ...")
#     time.sleep(15)


  
# print("Opening Messenger ...")
# driver.get('https://web.facebook.com/messages/t/{}?_rdc=1&_rdr'.format(IDLIST[0]))
# time.sleep(10)
# print("Messenger Loaded ... ")
# grid=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div")
# grid.find_elements_by_tag_name('div')[0].click()
# time.sleep(10)



# tracker=[]
# def contact_saver(data):
#     with open("fresh_fetched_contacts.txt", "w") as file:
#         for x in data:
#             file.write(str(x)+"\n")
    




# while True: 
#     target_html = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")
#     soup = BeautifulSoup(target_html.get_attribute("innerHTML"), 'lxml')
#     soup = soup.select('div.l9j0dhe7')
#     soup = [x.select('a.oajrlxb2.gs1a9yip.g5ia77u1') for x in soup]
#     soup = [x for x in soup if x!=[]]
#     soup=[str(x[0]['href']).split('/')[-2] for x in soup]
#     print(((soup)))
#     print(len((soup)))
#     tracker.append(len(soup))
    
    
#     if len(soup)>=minimum_contacts:
#         print("==> Criteria achieved.")
#         contact_saver(soup)
#         break
    
#     if len(tracker)>=10:
#         if tracker[-4]==tracker[-3]==tracker[-2]==tracker[-1]:
#             print("*** SAME")
#             contact_saver(soup)
#             break 
    
    
    
    
#     time.sleep(3)
#     moving_bars =driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]")

#     # print(len(moving_bars.find_elements_by_tag_name('div')))

#     felem = moving_bars.find_elements_by_tag_name('div')[0]
#     lelem = moving_bars.find_elements_by_tag_name('div')[-1]

    

#     time.sleep(3)
#     print("=> moving to last bar")
#     lelem.location_once_scrolled_into_view
#     # time.sleep(6)
#     # felem.location_once_scrolled_into_view






# # target_html = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")
# # soup = BeautifulSoup(target_html.get_attribute("innerHTML"), 'lxml')
# # print(len(str(soup)))

# # grid=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div")

# # soup = BeautifulSoup(grid.get_attribute("innerHTML"), 'lxml')
# # print(len(str(soup)))


# # time.sleep(5)

 
# # grid2=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")
 
# # grid2.element.location_once_scrolled_into_view




# # grid2 = grid2.get_attribute("innerHTML")
# # soup = BeautifulSoup(grid2, 'lxml')

# # print(soup)

# # ids = [x.select('a')[0]['href'] for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# # soup = [x.select('a')[0].select('span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5')[0].text.replace('\n','').strip() for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# # names = [re.sub(' +', ' ',x) for x in soup]
# # dictionary = dict(zip(names, ids))
# # print(dictionary)
# # print(len(ids))




        
# # file=''
# # file = open('tes.html', 'r').read()
# # soup = BeautifulSoup(file, 'lxml')
# # ids = [x.select('a')[0]['href'].replace('/messages/t/','')[:-1] for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# # soup = [x.select('a')[0].select('span.a8c37x1j.ni8dbmo4.stjgntxs.l9j0dhe7.ltmttdrg.g0qnabr5')[0].text.replace('\n','').strip() for x in soup.select('div.l9j0dhe7') if x.select('a')!=[]]
# # names = [re.sub(' +', ' ',x) for x in soup]
# # dictionary = dict(zip(names, ids))
# # [print(x, "__________" ,dictionary[x]) for x in dictionary]
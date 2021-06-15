from selenium import webdriver
import time,os,uuid,json,re,sched, timeit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random,time,getpass,csv
  
from api import SERVER_MESSAGE





chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
uindex=0


def BOT_THREAD_STARTER(driver,EMAILID,PASSWORD,your_id,minimum_contacts,max_wait_for_reply):
    global uindex
     
    try:
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

        from marketplace_contact_fetch import ContactFetcher

        # if os.path.exists(os.path.join(os.getcwd(),'fresh_fetched_contacts.txt')):pass
        # else: ContactFetcher(driver,int(your_id),int(minimum_contacts))
        ContactFetcher(driver,int(your_id),int(minimum_contacts))



        IDLIST = [] 
        with open('fresh_fetched_contacts.txt', 'r') as file:
            for line in file.readlines():
                IDLIST.append(str(line).strip())
                    
        MESSAGES_LOG=[ {"id":x,"sessional_len":0,"init_messgae_handler":0} for x in IDLIST]



        BOTINITTIME = int(time.time())
        total_received_messages = 0
        loop_counter=0





        while True:

            for index,TARGETCHATID in enumerate(IDLIST[:int(minimum_contacts)]):
                SESSIONAL_LEN = 0
                print("Opening Messenger ...")
                driver.get('https://web.facebook.com/messages/t/{}'.format(TARGETCHATID))
                print("Messenger Loaded ... ")
                time.sleep(20)
                HELLO_MESSAGE = "Hello. Is it still avaliable."

                def CHAT_CONTEXT_HANDLER(): 
                    try:
                        time_locker = time.time()

                        while True:   
                            print("** Refreshing Chat Inbox")
                            time.sleep(3)  
                            cclass="oo9gr5id"
                            mclass="ljqsnud1" 
                            body_soup = driver.find_element_by_tag_name("body")
                            soup = BeautifulSoup(str(body_soup.get_attribute("innerHTML")), 'lxml')
                            allmsgs = soup.select("div.ljqsnud1.g6srhlxm.odn2s2vf")
                            allmsgs = [[msg.select('div')[0].text,msg.select('div')[0].attrs['class']] for msg in allmsgs]
                            mymsgs = [x for x in allmsgs if mclass in x[-1]]
                            clientmsgs = [x for x in allmsgs if cclass in x[-1]]
                            hasclientreplied = True if mclass not in  allmsgs[-1][-1] else False
                            whosentlastmsg = ''
                            lastmsg_class = allmsgs[-1][-1]
                            if mclass in lastmsg_class :whosentlastmsg = "me"
                            elif mclass not in lastmsg_class:whosentlastmsg='client' 
                            

                            print("#"*20)
                            print(len(mymsgs))
                            print(len(clientmsgs))
                            print(whosentlastmsg)
                            print(hasclientreplied) 
                            print("-"*20)

                            print(mymsgs)

                            
                            if 'bye' in mymsgs[-1][0].lower():
                                print("bye is in message")
                                print(f"-->> bye is in message -- moving to next user")
                                break
                            else:
                                print("No BYE")






                            if len(clientmsgs)==0 and  len(mymsgs)==1:
                                print("Sending hello message")
                                textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
                                try: 
                                    for char in str(HELLO_MESSAGE):
                                        textAreaElem.send_keys(str(char))
                                        time.sleep(0.05)
                                    time.sleep(2)
                                    sender = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
                                    sender.click() 
                                except:
                                    print("stale element reference")
                                    continue


                                


                            elif whosentlastmsg=='me' and len(clientmsgs)==0:
                                print("** No Wait")
                                break

                            elif whosentlastmsg=='me':
                                if time.time()-time_locker>int(max_wait_for_reply):
                                    print("timer completed")
                                    break
                                else:
                                    print("__waiting")
                                     

                            elif whosentlastmsg=='client':
                                lastmsgtext = allmsgs[-1][0]
                                print(f"-->> API CALL for ( {lastmsgtext} )")
                                msg = SERVER_MESSAGE(str("unknown"),str(lastmsgtext))
                                print(f"-->> API Response ( {msg} )")

                                if str(msg).startswith('"') and str(msg).endswith('"'):
                                    msg = msg[1:-1] 

                                textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
                                try:
                                    for x in msg:
                                        textAreaElem.send_keys(str(x))
                                        time.sleep(0.05)  
                                    textAreaElem.send_keys(Keys.RETURN) 
                                    time_locker = time.time() 
                                except:
                                    print("stale element reference")
                            else:print("no condition meet")
                                    



                            
                            print("#"*20)  
                    except Exception as e:
                        print(e)
                        print(e.__traceback__.tb_lineno)

                CHAT_CONTEXT_HANDLER()



 
                
                

                
            #     # INITILIZATION OF CHAT BY BOT
            #     print("INITILIZATION OF CHAT BY BOT")
            #     time.sleep(2)
                
                
            #     textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
                
                    
            #     try:
            #         for log in MESSAGES_LOG:
            #             if log['id']== TARGETCHATID and log['init_messgae_handler']==0:   
            #                 firstmessage ="Hello ..."
            #                 for textindex, char in enumerate(firstmessage):
            #                     textAreaElem.send_keys(char)
            #                     time.sleep(0.05)
                                

            #                 sender = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            #                 sender.click()
            #                 log['init_messgae_handler']=1
                            
            #             # else:log['init_messgae_handler']=1
            #     except:print("stale element reference")
                
            #     def initer():
            #         global BOTINITTIME
            #         global total_received_messages
            #         global loop_counter
            #         BOTINITTIME = int(time.time())
            #         total_received_messages = 0
            #         loop_counter=0
            #         def CHATTER():
            #             global BOTINITTIME
            #             global total_received_messages
            #             global loop_counter
            #             global SESSIONAL_LEN
            #             loop_counter=loop_counter+1
            #             print("_______________________________________")
            #             print("_______________________________________")
            #             print("Loop__Counter__", loop_counter)
            #             time.sleep(5)
            #             print("Grabbing Chat Container ...") 
            #             textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
            #             chat_container = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div/div/div[3]')
            #             chats=chat_container.get_attribute('innerHTML')
            #             me ="ljqsnud1"
            #             friend="oo9gr5id"
            #             # we have to read friend mesage
            #             print("Making soup ....")
            #             soup = BeautifulSoup(chats, 'lxml') 
            #             received_messages = soup.select('div.oo9gr5id')
            #             sent_messages = soup.select('div.ljqsnud1')
            #             # QUERY = received_messages[-1].text
            #             try:
            #                 received_message_len=len(received_messages)
            #             except TypeError:
            #                 received_message_len=int(received_messages)
                        
                        
            #             print("Comparing the Results ...")
            #             print("Comaprison Result "+str(total_received_messages)+"_____"+str(received_message_len)) 
            #             SESSIONAL_LEN = received_message_len
            #             WAITING_INTERVAL=int(max_wait_for_reply)
            #             if  (time.time()-BOTINITTIME>=WAITING_INTERVAL):
            #                 if len(soup.select('div.oo9gr5id')) == total_received_messages:
            #                 # print("** firend didn't responnd in 30 seconds.. MOVING TO NEXT ")
            #                     return 'next'
                        
                        
            #             try:
            #                 try:
            #                     if received_message_len<total_received_messages:
            #                         total_received_messages,received_messages = received_messages,total_received_messages
            #                 except:pass
            #                 if total_received_messages<received_message_len:
                                
            #                     # INITILIZATION OF CHAT BY BOT
            #                     print("Sending new mesage ... ") 
            #                     QUERY = received_messages[-1].text
            #                     if received_message_len<1:
            #                         QUERY = "Hello " 
            #                     DATA_RECEIVED = json.loads(SERVER_MESSAGE("unknown",str(QUERY)))
            #                     total_received_messages=received_message_len
            #                     time.sleep(2) 
                                
                                
            #                     textAreaElem = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
            #                     try:
            #                         for log in MESSAGES_LOG:
            #                             if log['id']== TARGETCHATID and log['sessional_len']<received_message_len:
            #                                 for char in str(DATA_RECEIVED):
            #                                     textAreaElem.send_keys(str(char))
            #                                     time.sleep(0.05)
            #                                 time.sleep(2)
            #                                 sender = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
            #                                 sender.click()
            #                                 BOTINITTIME = int(time.time())
            #                     except:print("stale element reference")
                                
            #                     print ("Loop again Started ... new message", )
            #                     CHATTER()
            #                 time.sleep(2) 
            #                 CHATTER()      
            #             except TypeError:CHATTER()    
            #         CHATTER()
            #     initer()
            #     print("**__________________Moving to next Friend ")
            #     for log in MESSAGES_LOG:
            #         if log['id']== TARGETCHATID:
            #             log['sessional_len'] = SESSIONAL_LEN
            #     print(MESSAGES_LOG)
            #     uindex=index
            # # if int(uindex)==(len(IDLIST)-1):
            # #     driver.quit()
            # #     break
        return True
    except Exception as e:
        print(e)
        return False            



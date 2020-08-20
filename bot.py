import pyttsx3
import datetime
import os
import wikipedia
print("i am your assistant  \n how may i help you--")
while True  :
     p=input()
     if(("run"in p) or ("open" in p)) and("chrome" in p) :
         os.system("chrome")
     elif(("run"in p) or ("open" in p)) and("notepad" in p) :
         os.system("notepad")
     elif(("run"in p) or ("open" in p)) and("skype" in p) :
         os.system("skype")
     elif ("turnoff"in p) or ("turn off" in p)  :
         os.system("shutdown /s /t 1")
     elif(("say"in p) or ("what" in p)) and ("time" in p) :
         x = datetime.datetime.now()
         print(x.strftime("%X"))  
         pyttsx3.speak(x.strftime("%X"))
     elif(("say "in p) or ("what is" in p)) and("date" in p) :
         x = datetime.datetime.now()
         print(x.strftime("%x")) 
         pyttsx3.speak(x.strftime("%x"))
     elif("who is"in p) or("summary"in p): 
         result = wikipedia.summary(p, sentences = 3)
         print(result)
         pyttsx3.speak(result)
     elif ("tell me about"in p) or("say about" in p) or("told about" in p):
         spl_word="about"
         res =p.split() 
         ##(p.partition(spl_word)[2] ) -------------partition the sentance
         result = wikipedia.summary(p.partition(spl_word)[2], sentences = 3)
         print(result)
         pyttsx3.speak(result)
     elif(("how to"in p) or ("which is" in p) or ("sarch" in p) ):
         if("how to"in p) or ("which is" in p):
             a=p.replace(" ","+")
             os.system("chrome ""www.google.com/search?q="+a+"")
         else:
              x=input("what you want to sarch") 
              a=x.replace(" ","+")  
              os.system("chrome ""www.google.com/search?q="+a+"") 
     elif(("my name"in p) or ("you know my name" in p) or ("what is my name" in p) ) :
          if(("my name"in p) or ("you know my name" in p) or ("what is my name" in p) or("save my name") ):
              with open('name.py', 'a') as f:
               if f.tell() == 0:
                    print('say your name')
                    name= input()
                    print ("i remember ypor name "+name)
                    f=open("name.py","w")
                    f.write("c='"+name+"'")
                    f.close()
               elif("save my name"in p) or ("change my name"in p):
                    name=input("type name ")
                    print ("i remember ypor name "+name)
                    f=open("name.py","w")

                    f.write("c='"+name+"'")
                    f.close()
               else:
                    from name import c
                    print("u say that your name is  "+c)
     elif ("hay"in p) or("how are you" in p) or("hello" in p) or("hi" in p) :
         if("hay"in p)or("hello" in p)or("hi" in p):
             print("hello... i am your assistent.. ")
         else:
             print("i am fine") 
     elif ("save "in p)and(("pass"in p)or ("password"in p)):
         print("which password; ex-facebook,gmail etc")
         app=input("which password:")
         with open('password.txt', 'a') as f:
          if f.tell() == 0:
            print('enter your password\n')
            password=input()
            f.write(app+" :"+password+'\n')
            print("password saves")
          else:
            print('enter your passwor\n')
            password=input()
            f.write(app+" :"+password+'\n')
            print("password saves")
     elif ("pass"in p)or ("password"in p): 
         f = open("password.txt", "r")
         print(f.read())     
     elif (("stop"in p) or ("exit" in p)) or("stop pogram" in p):  
         break
     else:
         print("i can't understand '"+p+"'")  

     

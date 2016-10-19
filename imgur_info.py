from __future__ import print_function
import requests
import json
import re
import sys




maxp1 = 0
maxp2 = 0
maxp3 = 0
maxp4 = 0
maxp5 = 0

title1 = ""
title2 = ""
title3 = ""
title4 = ""
title5 = ""

hash1 = ""
hash2 = ""
hash3 = ""
hash4 = ""
hash5 = ""

datetime1 = ""
datetime2 = ""
datetime3 = ""
datetime4 = ""
datetime5 = ""

#page = requests.get(url)
print("Please enter a name: ", end = "")
name = raw_input()
num = 0
empty = ""
flag = 0
flag1 = 1
if __name__ == "__main__":
    url = "http://imgur.com/user/" + name + "/index/newest/page/" + str(num) + "/hit.json?scrolling"
    page = requests.get(url)
    check1 = re.findall("Zoinks! You've taken a wrong turn.", page.text)
    if check1:
        if (check1[0] == "Zoinks! You've taken a wrong turn."):
            print("This accout does not exist: " + name)
            flag1 = 2 
            flag = 1
    while(flag == 0):
        url = "http://imgur.com/user/" + name + "/index/newest/page/" + str  (num) + "/hit.json?scrolling"
        num = num + 1
        page = requests.get(url)
        check = re.findall('.*',page.text)
        ban = check[0]
        if(ban == ""):
            flag = 1
            break
        obj = json.loads(page.text)
        comment = obj["data"]["captions"]["data"]
        for d in comment:
            if(d["points"] >= maxp1):
                if(d["points"] == maxp1):
                    if(d["hash"] > hash1):
                        maxp5 = maxp4
            
                        hash5 = hash4
                        hash4 = hash3
                        hash3 = hash2
                        hash2 = hash1
                        hash1 = d["hash"]

                        title5 = title4
                        title4 = title3
                        title3 = title2
                        title2 = title1
                        title1 = d["title"]
            
                        maxp4 = maxp3 
                        maxp3 = maxp2
                        maxp2 = maxp1
                        maxp1 = d["points"]

                        datetime5 = datetime4
                        datetime4 = datetime3
                        datetime3 = datetime2
                        datetime2 = datetime1
                        datetime1 = d["datetime"]
                    elif(d["hash"] > hash2):
                        maxp5 = maxp4
                        maxp4 = maxp3
                        maxp3 = maxp2
                        maxp2 = d["points"]

                        hash5 = hash4
                        hash4 = hash3
                        hash3 = hash2
                        hash2 = d["hash"]
                  
                        title5 = title4
                        title4 = title3
                        title3 = title2
                        title2 = d["title"]

                        datetime5 = datetime4
                        datetime4 = datetime3
                        datetime3 = datetime2
                        datetime2 = d["datetime"]
                    elif(d["hash"] > hash3):
                        maxp5 = maxp4
                        maxp4 = maxp3
                        maxp3 = d["points"]
                        
                        hash5 = hash4
                        hash4 = hash3
                        hash3 = d["hash"]
                   
                        title5 = title4
                        title4 = title3
                        title3 = d["title"]
 
                        datetime5 = datetime4
                        datetime4 = datetime3
                        datetime3 = d["datetime"]
                    elif(d["hash"] > hash4):
                        maxp5 = maxp4
                        maxp4 = d["points"]
            
                        hash5 = hash4
                        hash4 = d["hash"]

                        title5 = title4
                        title4 = d["title"]

                        datetime5 = datetime4
                        datetime4 = d["datetime"]
                    elif(d["hash"] > hash5): 
                        maxp5 = d["points"]
                        hash5 = d["hash"]
                        title5 = d["title"]
                        datetime5 = d["datetime"] 
                else:
                    maxp5 = maxp4
                    
                    hash5 = hash4
                    hash4 = hash3
                    hash3 = hash2
                    hash2 = hash1
                    hash1 = d["hash"]

                    title5 = title4
                    title4 = title3
                    title3 = title2
                    title2 = title1
                    title1 = d["title"]
                 
                    maxp4 = maxp3
                    maxp3 = maxp2
                    maxp2 = maxp1
                    maxp1 = d["points"]

                    datetime5 = datetime4
                    datetime4 = datetime3
                    datetime3 = datetime2
                    datetime2 = datetime1
                    datetime1 = d["datetime"]      
            elif(d["points"] >= maxp2):
                if(d["points"] == maxp2):
                    if(d["hash"] > hash2):
                        maxp5 = maxp4
 
                        hash5 = hash4
                        hash4 = hash3
                        hash3 = hash2
                        hash2 = d["hash"]

                        title5 = title4
                        title4 = title3
                        title3 = title2
                        title2 = d["title"]
            
                        maxp4 = maxp3
                        maxp3 = maxp2
                        maxp2 = d["points"]

                        datetime5 = datetime4
                        datetime4 = datetime3
                        datetime3 = datetime2
                        datetime2 = d["datetime"]
                    else:
                        if(d["hash"] > hash3):
                            maxp5 = maxp4
 
                            hash5 = hash4
                            hash4 = hash3
                            hash3 = d["hash"]
       
                            title5 = title4
                            title4 = title3
                            title3 = d["hash"]

                            maxp4 = maxp3
                            maxp3 = d["points"]
 
                            datetime5 = datetime4
                            datetime4 = datetime3
                            datetime3 = d["datetime"]
                        elif(d["hash"] > hash4):
                            maxp5 = maxp4

                            hash5 = hash4
                            hash4 = d["hash"]

                            title5 = title4
                            title4 = d["title"]

                            maxp4 = d["points"]
 
                            datetime5 = datetime4
                            datetime4 = d["datetime"]
                        elif(d["hash"] > hash5):
                            maxp5 = d["points"]
                            hash5 = d["hash"]
                            title5 = d["title"]
                            datetime5 = d["datetime"]                           
                else:
                    maxp5 = maxp4
      
                    hash5 = hash4
                    hash4 = hash3
                    hash3 = hash2
                    hash2 = d["hash"]
               
                    title5 = title4
                    title4 = title3
                    title3 = title2
                    title2 = d["title"]

                    maxp4 = maxp3
                    maxp3 = maxp2
                    maxp2 = d["points"]
 
                    datetime5 = datetime4
                    datetime4 = datetime3
                    datetime3 = datetime2
                    datetime2 = d["datetime"]
            elif(d["points"] >= maxp3):
                if(d["points"] == maxp3):
                    if(d["hash"] > hash3):    
                        maxp5 = maxp4

                        hash5 = hash4
                        hash4 = hash3
                        hash3 = d["hash"]
      
                        title5 = title4
                        title4 = title3
                        title3 = d["title"]

                        maxp4 = maxp3
                        maxp3 = d["points"]

                        datetime5 = datetime4
                        datetime4 = datetime3
                        datetime3 = d["datetime"]
                    else:
                        if(d["hash"] > hash4):
                            maxp5 = maxp4

                            hash5 = hash4
                            hash4 = d["hash"]
                          
                            title5 = title4
                            title4 = d["title"]
   
                            maxp4 = d["points"]
                           
                            datetime5 = datetime4
                            datetime4 = d["datetime"]
                        elif(d["hash"] > hash5):
                            hash5 = d["hash"]
                            title5 = d["title"]
                            maxp5 = d["points"]
                            datetime5 = d["datetime"]
                            
 
                else:
                    maxp5 = maxp4
   
                    hash5 = hash4
                    hash4 = hash3
                    hash3 = d["hash"]

                    title5 = title4
                    title4 = title3
                    title3 = d["title"]

                    maxp4 = maxp3
                    maxp3 = d["points"]

                    datetime5 = datetime4
                    datetime4 = datetime3
                    datetime3 = d["datetime"]
            elif(d["points"] >= maxp4):
                if(d["points"] == maxp4):
                    if(d["hash"] > hash4):             
                        maxp5 = maxp4

                        hash5 = hash4
                        hash4 = d["hash"]

                        title5 = title4
                        title4 = d["title"]

                        maxp4 = d["points"]
               
                        datetime5 = datetime4
                        datetime4 = d["datetime"]
                    else:
                        if(d["hash"] > hash5):
                            hash5 = d["hash"]
                            title5 = d["title"]
                            maxp5 = d["points"]
                            datetime5 = d["datetime"]       
                else:
                    maxp5 = maxp4
                    
                    hash5 = hash4
                    hash4 = d["hash"]

                    title5 = title4
                    title4 = d["title"]

                    maxp4 = d["points"]
 
                    datetime5 = datetime4
                    datetime4 = d["datetime"]
            elif(d["points"] >= maxp5):
                if(d["points"] == maxp5):
                    if(d["hash"] > hash5): 
                        hash5 = d["hash"]
                        title5 = d["title"]
                        maxp5 = d["points"]
                        datetime5 = d["datetime"]
                else:
                    hash5 = d["hash"]
                    title5 = d["title"]
                    maxp5 = d["points"]
                    datetime5 = d["datetime"]
    if(maxp1 == 0):
        print("This account has no comments!")
    else:
        if(flag1 == 1):
            print("1. ", hash1)
            print("Points: ", maxp1)
            print("Title: ", title1)
            print("Date: ", datetime1)
            print("")
            print("2. ", hash2)
            print("Points: ", maxp2)
            print("Title: ", title2)
            print("Date: ", datetime2)
            print("")
            print("3. ",hash3)
            print("Points: ", maxp3)
            print("Title: ", title3)
            print("Date: ", datetime3)
            print("")
            print("4. ", hash4)
            print("Points: ", maxp4)
            print("Title: ", title4)
            print("Date: ", datetime4)
            print("")
            print("5. ", hash5)
            print("Points: ", maxp5)
            print("Title: ", title5)
            print("Date: ", datetime5)
            print("")
       






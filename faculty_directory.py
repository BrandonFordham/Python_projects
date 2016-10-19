from __future__ import print_function
import requests
import re
import sys

url = "http://www.cs.fsu.edu/department/faculty/"
main_page = requests.get(url)


link = re.findall(r'http://www.cs.fsu.edu/department/faculty/[a-zZ-Z]*/', main_page.text)


if __name__ == "__main__": 
    i = 0
    for word in link:
        url1 = link[i]
        main_page1 = requests.get(url1)
        name = re.findall('<title>[a-zA-Z]+.* [a-zA-Z]+', main_page1.text)
        link1 = re.findall('<td>.*?</td>',main_page1.text)
       # print(link1)
        i = i + 2
        s = name[0]
        namer = s.replace("<title>", "")
        n = namer
        nn = n.replace(" | Computer Science", "")        
        print("Name: ", nn)
        p = link1[1]
        officer = p.replace("<td>", "")
        pp = officer
        ppp = pp.replace("</td>", "")
        if ppp == "":
            print("Office: N/A")
        else:        
            print("Office: ",ppp)
        t = link1[3]
        telephoner = t.replace("<td>", "")
        tt = telephoner
        ttt = tt.replace("</td>", "")
        if ttt == "":
            print("Telephone: N/A")
        else:
            print("Telephone: ", ttt)      
        e = link1[4]
        emailr = e.replace("</td>", "")
        ee = emailr
        eee = ee.replace("<td>", "")
        print("Email: ", eee)
        print("*********************")
        if nn == "Peixiang Zhao":
            break
       
      
        """
        print("Building is ", link1[1])
        print("Phone is: ", link1[3])
        print("Email is: ", link1[4])
        print("*****************************")
        """        

              
    """
    print(link)
    print("hi")
    print(link[1])
    print(link1)
    print("BELOW")
    print("Name is : ", name[0])
    print("Building is: ", link1[1])
    print("Phone is: ", link1[3])
    print("Email is: ", link1[4])
    """

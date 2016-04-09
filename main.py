#
#  Programmer : Akshay Gore
#


from Book import Book
from SearchEngine import SearchEngine
from Media import Media
from Video import Video
from Periodic import Periodic
from Film import Film
import sys

search_result1=[]
search_result2=[]
search_result3=[]
search_result4=[]


flag = True
while flag:
    print("------------------------------------")
    print("1. Search by Call Number ")
    print("2. Search by Title ")
    print("3. Search by Subject ")
    print("4. Search by Other ")
    print("5. Quit ")
    n = input("\n Enter your Choice :  ")
    if n == "1":
        word = str(input("Enter the word to search :   "))
        s = SearchEngine()
        search_result1 = s.Search_call_number(word)
        for count in range(len(search_result1)):
            search_result1[count].display()
        del search_result1[:]

    elif n == "2":
        word = str(input("Enter the word to search :    "))
        s = SearchEngine()
        search_result2 = s.Search_title(word)
        for count in range(len(search_result2)):
            search_result2[count].display()
            #print("search_result2[count] :"+ str(len(search_result2)))
        del search_result2[:]

    elif n == "3":
        word = str(input("Enter the word to search :    "))
        s = SearchEngine()
        search_result3 = s.Search_subject(word)
        for count in range(len(search_result3)):
            search_result3[count].display()
        #print("search_result3[count] :"+ str(len(search_result3)))
        del search_result3[:]
    elif n == "4":
        word = str(input("Enter the word to search :    "))
        print(word)
        s = SearchEngine()
        search_result4 = s.Search_other(word)
        for count in range(len(search_result4)):
            search_result4[count].display()
        # print("search_result4[count] :"+ str(len(search_result4)))
        del search_result4[:]

    elif n == "5":
        flag = False
    else:
        print(" - -- - Invalid Input - -- - ")
        sys.exit()

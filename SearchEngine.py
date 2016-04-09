from Media import Media
from Book import Book
from Film import Film
from Video import Video
from Periodic import Periodic

class SearchEngine:
    """docstring for """

    def __init__(self):

        self.CardCatalog = list();
        book_list = ["callno","title","subject","author","description","publisher","city","year","series","notes"]
        fileObj = open("book.txt","r+")
        while True:
            # print('file read')
            line = fileObj.readline();
            if len(line)==0:
                break

            word = line.split('|');
            for count in range(10):
                book_list[count] = word[count].rstrip()

            book_obj = Book(book_list[0],book_list[1],book_list[2],book_list[3],book_list[4],book_list[5],book_list[6],book_list[9],book_list[8],book_list[9])

            self.CardCatalog.append(book_obj)

        fileObj.close()

        film_list = ["callno","title","subject","director","notes","year"]
        fileObj = open("film.txt","r+")
        while True:
            line = fileObj.readline();
            if len(line)==0:
                break
            word = line.split('|');
            for count in range(6):
                film_list[count] = word[count].rstrip()

            film_obj = Film(film_list[0],film_list[1],film_list[2],film_list[3],film_list[4],film_list[5])

            self.CardCatalog.append(film_obj)
        fileObj.close()

        video_list = ["callno","title","subject","description","distributor","notes","series","lable"]


        fileObj = open("video.txt","r+")
        while True:
            line = fileObj.readline();
            if len(line)==0:
                break
            word = line.split('|');
            for count in range(8):
                video_list[count] = word[count].rstrip()

            video_obj = Video(video_list[0],video_list[1],video_list[2],video_list[3],video_list[4],video_list[5],video_list[6],video_list[7])
            self.CardCatalog.append(video_obj)
        fileObj.close()


        periodic_list = ["callno","title","subject","author","description","publisher_hist","series","notes","related_title","other_title","gov_doc_no"]
        fileObj = open("periodic.txt","r+")
        while True:
            line = fileObj.readline();
            if len(line)==0:
                break
            word = line.split('|');
            for count in range(11):
                periodic_list[count] = word[count].rstrip()

            periodic_obj = Periodic(periodic_list[0],periodic_list[1],periodic_list[2],periodic_list[3],periodic_list[4],periodic_list[5],periodic_list[6],periodic_list[7],periodic_list[8],periodic_list[9],periodic_list[10])

            self.CardCatalog.append(periodic_obj)
        fileObj.close()


    def Search_call_number(self,keyword):
        Media_Result = [];
        for count in range(len(self.CardCatalog)):
            y = self.CardCatalog[count].compare_callno(keyword)
            if y == True:
                Media_Result.append(self.CardCatalog[count]);
        return Media_Result

    def Search_title(self,keyword):
        Media_Result = [];
        for count in range(0,len(self.CardCatalog)):
            y = self.CardCatalog[count].compare_title(keyword)
            if y == True:
                Media_Result.append(self.CardCatalog[count]);
        return Media_Result


    def Search_subject(self,keyword):
        Media_Result = [];
        for count in range(0,len(self.CardCatalog)):
            y = self.CardCatalog[count].compare_subject(keyword)
            if y == True:
                Media_Result.append(self.CardCatalog[count]);
        return Media_Result


    def Search_other(self,keyword):
        Media_Result = [];
        for count in range(0,len(self.CardCatalog)):
            y = self.CardCatalog[count].compare_other(keyword)
            if y == True:
                Media_Result.append(self.CardCatalog[count]);
        return Media_Result

from Media import Media
class Book(Media):
    """docstring for """
    def __init__(self,callno,title,subject,author,description,publisher,city,year,series,notes):
        Media.__init__(self,callno,title,subject,notes)
        self.author = author
        self.description = description
        self.publisher = publisher
        self.city = city
        self.year = year
        self.series = series


    def display(self):
        print("Media Type   -> Book")
        print("Call Number  ->"+ self.callno)
        print("Title        ->"+self.title)
        print("Subject      ->"+ self.subject)
        print("Author       ->"+self.author)
        print("Description  ->"+self.description)
        print("Publisher    ->"+self.publisher)
        print("City         ->"+self.city)
        print("Year         ->"+self.year)
        print("Series       ->"+self.series)
        print("Notes        ->"+self.notes)
        print("-----------------------------------------")

    def compare_other(self,keyword):
        combined_string = self.description +" " + self.notes  +" "+ self.year;
        if combined_string.find(keyword) != -1:
            return True
        else:
            return False

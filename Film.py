from Media import Media
class Film(Media):
    """docstring for """
    def __init__(self,callno,title,subject,director,notes,year):
        Media.__init__(self,callno,title,subject,notes)
        self.director=director
        self.year= year

    def display(self):
        print("Media Type  -> Film")
        print("Call Number ->"+self.callno)
        print("Title       ->" +self.title)
        print("Subject     ->" +self.subject)
        print("Notes       ->" +self.notes)
        print("Director    ->"+self.director)
        print("Year        ->"+self.year)
        print("-----------------------------------------")


    def compare_other(self,keyword):
        combined_string = self.notes + " "+self.director+" "+self.year
        if combined_string.find(keyword) != -1:
            return True
        else:
            return False

from Media import Media

class Video(Media):
    """docstring for """
    def __init__(self, callno,title,subject,description,distributor,notes,series,lable):
        Media.__init__(self,callno,title,subject,notes)
        self.description = description
        self.distributor = distributor
        self.series = series
        self.lable = lable

    def display(self):
        print( "Media Type     -> Video");
        print( "Call Number    ->"+self.callno);
        print( "Title          ->"+self.title);
        print( "Subject        ->"+self.subject);
        print( "Description    ->"+self.description);
        print( "Distributor    ->"+self.distributor);
        print( "Notes          ->"+self.notes);
        print( "Series         ->"+self.series);
        print( "Lable          ->"+self.lable);
        print( "-----------------------------------------");


    def compare_other(self,keyword):
        combined_string = self.description +" " + self.notes +" " + self.distributor;
        if combined_string.find(keyword) != -1:
            return True
        else:
            return False

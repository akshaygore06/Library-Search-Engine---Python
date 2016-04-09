from Media import Media

class Periodic(Media):
    """docstring for """
    def __init__(self,callno,title,subject,author,description,publisher_hist,series,notes,related_title,other_title,gov_doc_no):
        Media.__init__(self,callno,title,subject,notes)
        self.author =author
        self.description = description
        self.publisher_hist = publisher_hist
        self.series =series
        self.related_title =related_title
        self.other_title = other_title
        self.gov_doc_no = gov_doc_no


    def display(self):
        print("Media Type     -> Periodic");
        print("Call Number    ->"+ self.callno);
        print("Title          ->"+ self.title);
        print("Subject        ->"+ self.subject);
        print("author         ->"+ self.author);
        print("description    ->"+ self.description);
        print("publisher_hist ->"+ self.publisher_hist);
        print("Series         ->"+ self.series);
        print("Notes          ->"+ self.notes);
        print("Related Title  ->"+ self.related_title);
        print("Other_title    ->"+ self.other_title);
        print("Gov Doc Number ->"+ self.gov_doc_no);
        print("-----------------------------------------");


    def compare_other(self,keyword):
        combined_string = self.description +" " + self.notes +" " + self.series +" "+ self.related_title;
        if combined_string.find(keyword) != -1:
            return True
        else:
            return False

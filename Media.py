class Media:
    """docstring for """
    def __init__(self, callno,title,subject,notes):
        self.callno = callno
        self.title = title
        self.subject = subject
        self.notes = notes

    def compare_callno(self,keyword):
        if self.callno.find(keyword) != -1:
            return True
        else:
            return False

    def compare_title(self,keyword):
        if self.title.find(keyword) != -1:
            return True
        else:
            return False

    def compare_subject(self,keyword):
        if self.subject.find(keyword) != -1:
            return True
        else:
            return False


    def compare_other(self,keyword):
        return False

    def display(self):
        pass

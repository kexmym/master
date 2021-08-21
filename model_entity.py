class Reference: 
    def __init__(self, abstract, publication_year, title):
        self.abstract = abstract
        self.publication_year = publication_year
        self.title = title

    def print(self):
        print(f"ab : {self.abstract} \npy : {self.publication_year} \nti : {self.title}")

from abc import abstractmethod

class Reference:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def setter(self):
        pass

    @abstractmethod
    def set_a_matches(self):
        pass

    @abstractmethod
    def set_b_matches(self):
        pass

class Master_Reference(Reference):

    def __init__(self, abstract = "", publication_year = "", title = "", a_matches = False, b_matches = False):
        self.abstract = abstract
        self.publication_year = publication_year
        self.title = title
        self.a_matches = a_matches
        self.b_matches = b_matches

    def print(self):
        print(f"ab : {self.abstract} \npy : {self.publication_year} \nti : {self.title} \na_matches : {self.a_matches} \nb_matches : {self.b_matches}")

    def setter(self, abstract = "", publication_year = "", title = "", a_matches = False, b_matches = False):
        self.abstract = abstract
        self.publication_year = publication_year
        self.title = title
        self.a_matches = a_matches
        self.b_matches = b_matches
    
    def set_a_matches(self, a_matches : bool = False):
        self.a_matches = a_matches

    def set_b_matches(self, b_matches : bool = False):
        self.b_matches = b_matches

    def get_a_matches(self):
        return self.a_matches

    def get_b_matches(self):
        return self.b_matches    

class Secondary_Reference(Reference):

    def __init__(self, abstract = "", publication_year = "", title = ""):
        self.abstract = abstract
        self.publication_year = publication_year
        self.title = title

    def print(self):
        print(f"ab : {self.abstract} \npy : {self.publication_year} \nti : {self.title}")

    def setter(self, abstract = "", publication_year = "", title = ""):
        self.abstract = abstract
        self.publication_year = publication_year
        self.title = title

    def set_a_matches(self, a_matches : bool = False):
        self.a_matches = a_matches

    def set_b_matches(self, b_matches : bool = False):
        self.b_matches = b_matches
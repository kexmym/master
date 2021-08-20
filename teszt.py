class Reference: 
    def __init__(self, ab, py, ti):
        self.ab =ab
        self.py =py
        self.ti =ti

    def print(self):
        print(f"ab : {self.ab} \npy : {self.py} \nti : {self.ti}")


end_of_line = "ER"
reference_list = []

f = open("text.txt", "r", encoding="utf8")
for x in f:
    if x[0:2] == "AB":
        abstract=x[6:]
    if x[0:2] == "PY":
        publication_year=x[6:]
    if x[0:2] == "TI":
        title=x[6:]
    if x[0:2] == end_of_line:
        reference = Reference(abstract,publication_year,title)
        reference_list.append(reference) 

for x in reference_list:
    x.print()


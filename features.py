from model_entity import Reference

def read_datas():
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

    return reference_list
stuff = [4,"tom",1,"michael",5,7,"Jimmy Smith"]
for element in stuff:
    if isinstance(element,int):
        print "*" * element
    elif isinstance(element, str):
        letter = element[0]
        print letter * len(stuff)
    else:
        pass
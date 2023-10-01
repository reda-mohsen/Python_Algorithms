"""
prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
names with commas and one and, as in the below:
    Adieu, adieu, to Liesl
    Adieu, adieu, to Liesl and Friedrich
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""

import inflect

p = inflect.engine()
list = ["Adieu", "adieu"]
try:
    counter = 0
    while True:
        if counter == 0:
            name = input("Name: ")
            list.append("to "+name)
            counter +=1
        else:
            name = input("Name: ")
            list.append(name)
            counter +=1
except EOFError:
    if counter == 0:
        print()
        pass
    elif counter == 1 :
        l = ""
        for i in range(2):
            l += list[i] + ", "
        l += list[2]
        print(l)
    elif counter == 2:
        mylist = p.join(list,final_sep="")
        print()
        print(mylist)
    else:
        mylist = p.join(list,final_sep=",")
        print()
        print(mylist)

import re

regex = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if (re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


check("hmtm.cse@gmail.com")
check("hmtm.cse@gmail.solution")
check("hmtm-cse@gmail.solution")
check("hmtm_cse@gmail.solution")
check("hmtm$cse@gmail.solution")
check("hmtm+cse@gmail.solution")
check("hmtm%cse@gmail.solution")

import itertools

ml1 = ["Hello, ", "Good Morning, "]
ml2 = ["I hope you are well. ", "Hope you are well. "]
ml3 = ["My name is John ", "My name is Tom "]
ml4 = ["and I am reaching out to you on behalf of S2Grupo.  ",
       "and I am reaching out to you on behalf of HP. "]
ml5 = ["We are currently looking to hire ", "We are currently looking to recruit "]
ml6 = ["someone ", "a worker  "]
ml7 = ["for the role of Cibersecurity Engineer ", "for the role of Blockchain Engineer "]
ml8 = ["and after reviewing your resume and experience, ", "and after reviewing your Linkedin, "]
ml9 = ["we believe that you would be a great fit for this position. ",
       "we believe that you would be a great fit for this job. "]
ml10 = ["At Company, we pride ourselves on our dynamic ",
        "At Company, we pride ourselves on our productive "]
ml11 = ["and collaborative work environment. ", "and cooperative work environment. "]
ml12 = [
    "Therefore, It is my pleasure to contact you today to inform you of the opportunity we have for you. ",
    "This is why It is a privilege to contact you to let you know about the incredible opportunity we have for you. "]
ml13 = ["You have proven to be a reliable person for us, ",
        "You have reaffirmed that you are a person we can trust, "]
ml14 = ["and I know that you will be able to help us make this innovative project a success. ",
        "and I know that you will be able to make our future project a success. "]
ml15 = ["I am writing to you ", "I am sending you this email  "]
ml16 = ["because I have recently become aware of your experience and expertise. ",
        "because I have just recently become aware of your experience, skills and knowledge. "]
ml17 = ["If they are correct, ", "If they are true,  "]
ml18 = ["I would like to offer you ", "I would like to propose you "]
ml19 = ["the job in our company. ", "the possibility of a job in our company. "]
ml20 = ["Our current salary range ", "Our actual salary range "]
ml21 = ["for this type of position is $100,000/year. Do you accept the agreement? ", "for this type of role is $200,000/year. Do you accept the deal? "]
ml22 = ["Regards.", "Best Regards."]

result = list(itertools.product(ml1, ml2, ml3, ml4, ml5, ml6, ml7, ml8, ml9, ml10, ml11, ml12, ml13, ml14, ml15, ml16, ml17, ml18, ml19, ml20, ml21, ml22))

# Si quieres puedes recorrer el resultado para ver las combinaciones

print(len(result))
for comb in result:
    print("".join(comb))
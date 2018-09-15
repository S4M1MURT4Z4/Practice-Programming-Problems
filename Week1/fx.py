q1 = lambda x:"".join(("*"*(max ([len(i) for i in x])+2)+"\n")+ "".join(["*"+i.ljust(max ([len(i) for i in x]))+"*\n" for i in x]) +("*"*(max ([len(i) for i in x])+2)+"\n"))
q2 = lambda :"".join([line for line in open("99.txt")])


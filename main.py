from textRewriter import TextRewriter



sentences = ['AP Computer Science is a college-level computer science course','that introduces object-oriented programming and design','using the Java programming language.','Students develop an understanding of coding through analyzing, writing, and testing code', 'as they explore concepts like modularity, variables, and control structures.', 'Fundamental topics in this course develop computational thinking skills', 'through the design of solutions to problems,', 'the use of data structures to organize large sets of data,','the development and implementation of algorithms to process data and discover new information,', 'the analysis of potential solutions, and the ethical and social implications of computing systems.']
for sentence in sentences:
    new_sentence = TextRewriter(sentence).run() 
    print(sentence + " -> " + new_sentence)
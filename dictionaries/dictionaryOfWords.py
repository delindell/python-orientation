word_definitions = dict()
word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Creative"] = "A state of being that arrives when one enjoys multiple beers"
word_definitions["Rascal"] = "Person or thing that behaves in a somewhat undesirable manner"
word_definitions["Squirrel"] = "Tree rat"
word_definitions["Folder"] = "Something you make to store all your files in"

print(word_definitions["Awesome"])
print(word_definitions["Creative"])

for word, definition in word_definitions.items():
    print('The definition of %s is %s' % (word, definition))


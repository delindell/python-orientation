# Py 101

sum = 2 + 2

print("the value of sun is", sum)

name = "fred"

# print(monkey)

def say_name():
  global name
  name = "Linda"
  print("internal", name)

say_name()  
print("external", name)

# if/else

name = "Larry"
if name == "Linda":
    print("I am Linda. Larry is on vacation.")
elif name == "Fred":
    print("welcome to costco. I am Fred")
else:
    print("I am Larry")

# String interpolation
print(f"My name is {name}")

# No type coercion
# print(2 + "2")  no work!

"hello" + "world"
2 + 4

# Collections!
# arrays nope and objects yes! but....

# list // like arrays in JS
more_stuff = [2, "things", True] #booleans are capitalized

more_stuff.append("wow!")
print(more_stuff[2]) #prints True
print(more_stuff[-1]) #prints wow! // last value in list

more_stuff.insert(0, "sorry") # index where to add plus thing you want to add
print(more_stuff)

more_stuff.extend([45, False, "blah"])
print(more_stuff)

# python: dictionary // like objects in JS
# can have keys that are not strings
stuff = {"name": "Amanda", "category": "Manager", 20: "wtf?"}

# Reassign values
stuff["name"] = "Sally"
print(stuff["name"])

# Assign new properties
stuff["salary"] = "60,000"
print(stuff)

# Nested values
stuff["address"] = {"street": "sesame", "num": 123}
print(stuff)

print(stuff["address"]["street"])

# sets
junk = {"Curlies", "lies", 32, None}

junk.add("more Stuff")
print(junk)

names = ["joe", "linda", "fred", "linda"]
print(names)

example = set()
example.add("hello")
print(example)

names = list(set(names))
print(names)

colors = []
print(colors)

# empty dict
addresses = {}
addresses["num"] = 123
print(type(addresses))

# tuple is cool because it's immutable (can access values, just not change them)
my_tup = (1,2,3, "hello")
print(my_tup)

# How does it know it's a tuple?
my_tup = (12,) # the comma 
print(type(my_tup))

# loops
# for ... in

my_tup = (1,2,3, "hello")
my_set = {1, 2, 3}
junk = {"Curlies", "lies", 32, None}

for foo in junk:
    print(f"why is {foo} still in  here?")

for foo in my_tup:
    print(f"this is in my tup: {foo}")

my_dict = {
    123: "number",
    "name": "Broomhilda"
}

for foo in my_dict:
    print(f"What is the key? {foo}") #keys

for foo in my_dict.values():
    print(f"What is the value of {foo}") #values

for foo in my_dict.items():
    print(f"what are the keys and values? {foo}") # keys & values

# slicing
my_list = [1, 2, 3, 'hello', 'monkey']
# JS way
# let my_subset = my_list.slice(0, 3)

my_subset = my_list[1:3]
print(my_subset)
my_subset = my_list[:3]
my_subset = my_list[3:]
print(my_subset)

# What kind of file is this?
print('name', __name__)


if  __name__ == "__main__":
        print('shut up bro')

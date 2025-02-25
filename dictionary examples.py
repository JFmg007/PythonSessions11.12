d={} # empty dictionary
eng_to_span={"one":"uno","two":"dos","three":"tres"}
print(eng_to_span)
eng_to_span["i"]="yo"
eng_to_span["am"]="soy"
eng_to_span["spanish"]="espanol"
print(eng_to_span)
sentence="i am spanish"
words=sentence.split()
for word in words:
    print(eng_to_span[word])
eng_to_span.update({"yes":"si","no":"no"}) # update a dictionary with a new dictionary
print(eng_to_span)
del eng_to_span["no"]
print(eng_to_span)

# print(eng_to_span.popitem()) not very useful since it is hard ot know which is the last item
print(eng_to_span.pop("two")) # much better to pop value by specifying the key

if "tree" in eng_to_span:
    print(eng_to_span["tree"])
else:
    print("I don't know that word")

print(eng_to_span.get("tree", "unknown word"))

for key in eng_to_span:
    print(f"{eng_to_span[key]} means {key}")

for key, value in eng_to_span.items(): # same thing only a bit simpler
    print(f"{value} means {key}")
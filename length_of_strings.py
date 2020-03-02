languages = ["English", "French", "Python", "Ruby",
             "Portuguese", "Italian", "Javascript", "C"]
keep = []
for l in languages:
    count = len(l)
    keep.append(count)
print(keep)

counts2 = [len(l) for l in languages]
print(counts2)

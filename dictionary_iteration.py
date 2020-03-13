file_counts = {"jpg": "10", "gif": "15", "txt": "65", "csv": "23"}

for txt in file_counts.keys():
    for nums in file_counts.values():

        print("{} have {}".format(txt, nums))

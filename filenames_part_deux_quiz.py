

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_name = [old_name.replace('.hpp', '.h')for old_name in filenames]
newfilenames = [(filenames[i], new_name[i]) for i in range(0, len(filenames))]

# Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
print(newfilenames)


# should print[("program.c","program.c"),("stdio.hpp","stdio.h") etc]
print(newfilenames)

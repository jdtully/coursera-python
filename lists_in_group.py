def group_list(group, users):
    members = ", ".join(users)

    return group + members


print(group_list("marketing", ["jimmy", "sally", "bobo"]))

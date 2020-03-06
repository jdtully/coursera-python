def groups_per_user(group_dictionary):
    user_groups = {}
    for groups, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:

                user_groups[user] = [groups]

            else:

                user_groups[user].append(groups)

    return(user_groups)


print(groups_per_user(
    {"local": ["admin", "user1"], "public": ["admin", "userb"]}))

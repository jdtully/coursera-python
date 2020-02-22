teams = ['dragons', 'Imps', 'Faeries ', 'Cats']
for home in teams:
    for away in teams:
        if home != away:
            print(home + " & " + away)

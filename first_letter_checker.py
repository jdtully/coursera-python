names = ['Kira',
         'Mireya',
         'Julie',
         'Brynlee',
         'Haleigh',
         'Lailah',
         'Tara',
         'Marianna',
         'Makayla',
         'Jaidyn',
         'Kyla',
         'Aniya',
         'Alyson',
         'Ryann',
         'Kiley',
         'Maddison',
         'Livia',
         'Reese',
         'Cindy',
         'Leila']
list = []
for i in names:
    if i.startswith("K"):
        list.append(i)
print(list)

list = [i for i in names if i.startswith("K")]
print(list)

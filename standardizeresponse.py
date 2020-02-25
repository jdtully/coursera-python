def standardize(response):
    strip_response = response.strip()
    final = strip_response.lower()
    return final


print(standardize(input("what is your  response?")))

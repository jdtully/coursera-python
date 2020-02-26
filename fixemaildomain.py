def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@")
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email + "true"


print(replace_domain("jeff@bob.com", "", "bob.com", "", "jeff.com", ""))

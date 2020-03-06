def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            person = user+"@"+domain
            emails.append(person)
        return (emails)


print(email_list({"gmail.com": ["clark.kent", "lois.lane", "Jimmy.Oleson"]}))

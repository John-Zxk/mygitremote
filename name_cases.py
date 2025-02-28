message = "Hello Eric, would you like to learn some Python today?"
print(message)

first_name = 'ada'
last_name = 'love'
full_name = f"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())


message = 'Albert Einstein once said, “A person who never made a mistake never \ntried anything new.”'
print(message)

famous_person = "Albert Einstein once said"
message = "A person who never made a mistake never \ntried anything new."
print(f"{famous_person},{message}")


famous_person = "  Albert Einstein\n\tonce said  "
print(famous_person.rstrip())
print(famous_person.lstrip())
print(famous_person.strip())



filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

# Uporabnik vnese stavek.
# Program prešteje samoglasnike.

statement = input('Vnesi stavek:')

count = 0
for char in statement.lower():
    if char in 'aeiou':
        count += 1

print(f'V stavku je {count} samoglasnikov.')
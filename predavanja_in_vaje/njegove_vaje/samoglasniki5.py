# Uporabnik vnese stavek.
# Program prešteje samoglasnike.

statement = input('Vnesi stavek:')

count = 0
for char in statement:
    if char in 'aeiouAEIOU':
        count += 1

print(f'V stavku je {count} samoglasnikov.')
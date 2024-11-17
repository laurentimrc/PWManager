import secrets
import json
import os

# Funzione per generare una password complessa
def generate_password(length=12):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Funzione per salvare le password in un file JSON
def save_password(website, username, password, filename='passwords.json'):
    data = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

    data[website] = {'username': username, 'password': password}

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print(f'Password salvata per {website}')

# Esempio di utilizzo
if __name__ == '__main__':
    website = input('Inserisci il nome del sito web o dels servizio: ')
    username = input('Inserisci nome utente:')
    length = int(input('Inserisci la lunghezza della password (default 12): ') or 12)

    new_password = generate_password(length)
    save_password(website, username, new_password)

    print(f'Password generata per {website}: {new_password}')

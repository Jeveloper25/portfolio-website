import requests
import hashlib
import sys


def request_api_data(query_char: str):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, check the api and try again.')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwn_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwn_api_check(password)
        if count:
            return f'{password} was found {count} times.\nRecommend changing passwords'
        else:
            return f'{password} was not found.\nPassword is secure.'


def terminal_main(args):
    for password in args:
        count = pwn_api_check(password)
        if count:
            print(f'{password} was found {count} times.\nRecommend changing passwords')
        else:
            print(f'{password} was not found.\nPassword is secure.')
    return 'Process finished.'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

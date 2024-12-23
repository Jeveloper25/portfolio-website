code = {
    "password_security": """
    <code>
        import math
        import re
        from static.project_files.password_breach import pwn_api_check


        class Password:
            def __init__(self):
                self.password = ""
                self.length = 0
                self.char_set = set()
                self.char_set_size = 0
                self.entropy = 0
                self.security_score = 0

            def set_password(self, password: str):
                self.password = password
                self.length = len(self.password)

            def set_char_set(self):
                for char in self.password:
                    self.char_set.add(char)
                self.char_set_size = len(self.char_set)

            def set_entropy(self):
                self.entropy = round(math.log(self.char_set_size * self.length, 2), 2)
                self.security_score += self.entropy
                self.security_score = round(self.security_score, 2)

            def analyze_symbols(self):
                symbols = re.findall(r"[!@#$%^&*()_\\-0-9]", self.password)
                self.security_score += len(symbols) * 1.2
                self.security_score = round(self.security_score, 2)

            def analyze_leaks(self):
                leak_count = int(pwn_api_check(self.password))
                self.security_score -= math.log(leak_count) if leak_count > 0 else 0
                self.security_score = round(self.security_score)

            def get_password_strength(self):
                strength = ""
                if self.security_score > 15:
                    strength = "Amazing"
                elif self.security_score > 10:
                    strength = "Very Good"
                elif self.security_score > 7:
                    strength = "Good"
                elif self.security_score > 5:
                    strength = "Alright"
                elif self.security_score > 3:
                    strength = "Poor"
                else:
                    strength = "Very Poor"
                return strength

            def config(self, password: str):
                self.set_password(password)
                self.set_char_set()
                self.set_entropy()
                self.analyze_symbols()
                self.analyze_leaks()
    </code>
    """,
    "password_breach": """
    <code>
        import requests
        import hashlib
        import sys


        def request_api_data(query_char: str):
            url = "https://api.pwnedpasswords.com/range/" + query_char
            response = requests.get(url)
            if response.status_code != 200:
                raise RuntimeError(f"Error fetching: {response.status_code}, check the api and try again.")
            return response


        def get_password_leaks_count(hashes, hash_to_check):
            hashes = (line.split(":") for line in hashes.text.splitlines())
            for h, count in hashes:
                if h == hash_to_check:
                    return count
            return 0


        def pwn_api_check(password):
            # check password if it exists in API response
            sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
            first5char, tail = sha1password[:5], sha1password[5:]
            response = request_api_data(first5char)
            return get_password_leaks_count(response, tail)
    </code>
    """,
    "About": """
    <div class="col-4 col-12-medium">
        <p>
        Through my exploration into engineering, the software
        discipline emerged as not only the most important to learn
        but the most fun to engage with. It is for that reason that
        I chose to study Computer Systems Engineering. A benefit of
        going down the software route is that it allows a single
        individual to create such a wide breadth of technologies
        using nothing more than their own computer.
        </p>
    </div>
    <div class="col-4 col-12-medium">
        <p>
        This brings us to this website. The purpose of this website
        is to host and document my various projects as I create
        them. For the moment, it documetns only a very small amount
        of projects, but as time goes on I believe it will become a
        great reflection of my journey as a Computer Systems
        Engineer. The website itself is also one such project, using
        a pre-made html/css template and a Flask server. It will
        continue to be updated and refined as new projects are
        created.
        </p>
    </div>
""",
}

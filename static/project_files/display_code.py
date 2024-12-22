code = {
    'password_security': 
    """
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
                symbols = re.findall(r'[!@#$%^&*()_\\-0-9]', self.password)
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
    'password_breach': 
    """

    """
}
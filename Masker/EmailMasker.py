class EmailMasker:
    def __init__(self, email, mask_char="x"):
        self.email = email
        self.mask_char = mask_char

    def mask(self):
        local_part, domain = self.email.split("@")
        masked_local = self.mask_char * len(local_part)
        return f"{masked_local}@{domain}"
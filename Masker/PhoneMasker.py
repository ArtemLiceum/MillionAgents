class PhoneMasker:
    def __init__(self, phone, mask_char="x", mask_length=3):
        self.phone = phone
        self.mask_char = mask_char
        self.mask_length = mask_length

    def mask(self):
        trimmed_phone = " ".join(self.phone.split())
        digit_count = sum(1 for char in trimmed_phone if char.isdigit())
        visible_digits = max(digit_count - self.mask_length, 0)
        masked_phone = ""
        digit_counter = 0

        for char in trimmed_phone:
            if char.isdigit():
                if digit_counter < visible_digits:
                    masked_phone += char
                    digit_counter += 1
                else:
                    masked_phone += self.mask_char
                    digit_counter += 1
            else:
                masked_phone += char
        return masked_phone
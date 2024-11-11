class SkypeMasker:
    def __init__(self, skype_id, mask_char="x"):
        self.skype_id = skype_id
        self.mask_char = mask_char

    def mask(self):
        if self.skype_id.startswith("<a href=\"skype:"):
            start = self.skype_id.find("skype:") + 6
            end = self.skype_id.find("?", start)
            if end == -1:
                end = len(self.skype_id)
            masked_skype = self.skype_id[:start] + (self.mask_char * 3) + self.skype_id[end:]
        elif self.skype_id.startswith("skype:"):
            masked_skype = "skype:" + (self.mask_char * 3)
        else:
            raise ValueError("Invalid Skype format")
        return masked_skype
from EmailMasker import EmailMasker
from PhoneMasker import PhoneMasker
from SkypeMasker import SkypeMasker


if __name__ == '__main__':
    email = EmailMasker("example@example.com")
    print(email.mask())

    phone = PhoneMasker("+7   666  777     888", mask_char="Ъ", mask_length=4)
    print(phone.mask())

    skype_id = SkypeMasker("skype:alex.max")
    print(skype_id.mask())

    skype_link = SkypeMasker('<a href="skype:alex.max?call">skype</a>')
    print(skype_link.mask())

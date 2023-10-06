import random


def send_otp_code(phone_number, code):
    print("*" * 120)
    print("Verification Code:")
    print(f"{phone_number}: {code}")
    print("*" * 120)


def set_otp(phone_number):
    random_code = random.randint(1000, 9999)
    send_otp_code(phone_number=phone_number, code=random_code)
    return random_code

def format_phone(phone_number: str) -> str:

    digits = ''.join(filter(str.isdigit, phone_number))

    if len(digits) == 11 and digits.startswith('89'):
        formatted_phone_number = f"8 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}"
    elif len(digits) == 10 and digits.startswith('9'):
        formatted_phone_number = f"8 ({digits[:3]}) {digits[3:6]}-{digits[6:8]}-{digits[8:10]}"
    elif len(digits) == 11 and digits.startswith('79'):
        formatted_phone_number = f"8 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}"
    elif len(digits) == 12 and digits.startswith('79'):
        formatted_phone_number = f"8 ({digits[2:5]}) {digits[5:8]}-{digits[8:10]}-{digits[10:12]}"
    else:
        formatted_phone_number = digits

    return formatted_phone_number

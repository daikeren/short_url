from django.conf import settings

code = 'AP96YKVoviNBM2E1bmgrzcnRWalGZJFQ3Xsxq7L8kIduT540hpDwSCtfOjyHeU'


def generate_code(value):
    code = settings.SECRET_CODE
    length = len(code)
    val = int(value)

    result = ""

    while val > 0:
        d = val % length
        result = result + code[(d ^ 0xff) % length]
        val = int(val / length)

    if len(result) < 6:
        result += code[0] * (6 - len(result))

    return result

import requests
import random
from django.conf import settings

def send_otp_tophone(phone_no):
    try:
        otp=random.randint(1000, 9999)
        url=f'https://2factor.in/API/V1/:{settings.API_KEY}/SMS/:phone_number/AUTOGEN/:otp_template_name'
        response=requests.get(url)
        return otp
    except Exception as ex:
        return None

  
import requests
import random
import hashlib

# Generate a unique identifier for the request
asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

# Headers for the request
headers = {
    "clientsecret": 'lvc22mp3l1sfv6ujg83rd17btt',
    "user-agent": 'Truecaller/12.34.8 (Android;8.1.2)',
    "accept-encoding": 'gzip',
    "content-type": 'application/json; charset=UTF-8',
    "Host": 'account-asia-south1.truecaller.com'
}

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

def send_otp(phone_number):
    data = {
        "countryCode": "eg",
        "dialingCode": 20,
        "installationDetails": {
            "app": {
                "buildVersion": 8,
                "majorVersion": 12,
                "minorVersion": 34,
                "store": "GOOGLE_PLAY"
            },
            "device": {
                "deviceId": md5,
                "language": "ar",
                "manufacturer": "Xiaomi",
                "mobileServices": ["GMS"],
                "model": "Redmi Note 8A Prime",
                "osName": "Android",
                "osVersion": "7.1.2",
                "simSerials": ["8920022021714943876f", "8920022022805258505f"]
            },
            "language": "ar",
            "sims": [
                {"imsi": "602022207634386", "mcc": "602", "mnc": "2", "operator": "vodafone"},
                {"imsi": "602023133590849", "mcc": "602", "mnc": "2", "operator": "vodafone"}
            ],
            "storeVersion": {
                "buildVersion": 8,
                "majorVersion": 12,
                "minorVersion": 34
            }
        },
        "phoneNumber": phone_number,
        "region": "region-2",
        "sequenceNo": 1
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('status') == 40003:
            print('Invalid phone number.')
        else:
            phonum = response_data.get('parsedPhoneNumber')
            coucode = response_data.get('parsedCountryCode')
            print(f'Arama başarıyla gönderildi✓.: {phonum}, Ülke kodu : {coucode}.')
    else:
        print('Failed to send OTP.')

phone_number = input("Telefon numarasını gir örn; +905555555555): ")
send_otp(phone_number)

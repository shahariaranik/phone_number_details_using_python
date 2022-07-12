import phonenumbers
from phonenumbers import timezone,geocoder,carrier

while True:
    phone = phonenumbers.parse(input("enter the phone number for detais with county code:")) #put the country code with + example +880 for bangladesh
    print(phone)  
    print(timezone.time_zones_for_number(phone))
    print(carrier.name_for_number(phone,"en"))
    print(geocoder.description_for_number(phone,"en"))

    while True:
        userin = input("Want to try again?")
        if userin not in {"yes","no"}:
            continue
        else:
            break
    
    if 'no' == userin:
        break
    elif 'yes' == userin:
        continue

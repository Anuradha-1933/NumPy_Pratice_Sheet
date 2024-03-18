import phonenumbers
from  phonenumbers import geocoder
phone_number1=phonenumbers.parse("+918765524958")
phone_number2=phonenumbers.parse("+919336361034")
print("\n Phone Number Location")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
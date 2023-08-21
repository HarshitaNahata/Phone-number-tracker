import phonenumbers

#timezone is for telling the exact time of the area where the SIM actually is

#geocoder is for providing the service to check the SIM

#carrier does all the work related to SIM

from phonenumbers import timezone,geocoder,carrier

#Take phone number as input from user as a string and there should be a representaion of the country as well like +91 for India

ph_number=input("Enter your phone number with +__: ")

detail=phonenumbers.parse(ph_number)
#parse will give the details of the phone number

time=timezone.time_zones_for_number(detail)

carr_ier=carrier.name_for_number(detail,"en")
#"en" is used to display the name of company in english

reg=geocoder.description_for_number(detail,"en")

print(detail)
print(time)
print(carr_ier)
print(reg)
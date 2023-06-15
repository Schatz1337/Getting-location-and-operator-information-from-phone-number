import phonenumbers

numara1 = '+14103424322'
numara2 = '+905322424322'

# Lokasyon bilgisi için; "numara1" değişkenine bilgi almak istediğimiz numarayı giriyoruz.
from phonenumbers import geocoder
number = phonenumbers.parse(numara1)
print(geocoder.description_for_number(number, 'tr'))

# Operatör bilgisi için; "numara1" değişkenine bilgi almak istediğimiz numarayı giriyoruz.
from phonenumbers import carrier
number = phonenumbers.parse(numara1)
print(carrier.name_for_number(number, 'tr'))

# Zaman dilimi bilgisi için; "numara1" değişkenine bilgi almak istediğiniz numarayı giriyoruz.
from phonenumbers import timezone
number = phonenumbers.parse(numara1)
print(timezone.time_zones_for_number(number))

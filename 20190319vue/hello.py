# class Company:
#     def __init__(self,employee_list):
#         self.employee=employee_list
#     def __getitem__(self,item):
#         return self.employee[item+1]

# company=Company([1,2,3,"abc","def"])
# for i in company:
#     print(i)
from geopy.geocoders import Nominatim
# thermometr
geolocator = Nominatim()
location = geolocator.geocode("天安门")
print(location.address)

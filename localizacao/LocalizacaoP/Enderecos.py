from pygeocoder import Geocoder

endereco = "avenida paulista, 100 Sao paulo"
result = Geocoder("CHAVE_API").geocode(endereco)

#Geocoder("api").geocode(endereco).state
#Geocoder("api").geocode(endereco).postal_code
#Geocoder("api").geocode(endereco).country
#Geocoder("api").geocode(endereco).coordinates
#Geocoder("api").reverse_geocode(123123123, 13123123)


print(result)
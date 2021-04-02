<<<<<<< HEAD
import requests
url = 'http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
service_key="t0EiubcVT8TvICxW4e0wQVifJYkvuEW8paf7BSQYPZ%2FMAqJo%2BFXwWwDq6xUzg7CQ5h2JlIb06ASNlQSOVQdsqw%3D%3D"
service_key_decoded =requests.utils.unquote(service_key)
req_parameter ={"ServiceKey":service_key_decoded,"searchSe":"road","srchwrd":"반포대로 201"}
result =requests.get(url,params=req_parameter)
print(result.text)

import xmltodict
dict_data = xmltodict.parse(result.text)
print(dict_data)
=======
import requests
url = 'http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd'
service_key="t0EiubcVT8TvICxW4e0wQVifJYkvuEW8paf7BSQYPZ%2FMAqJo%2BFXwWwDq6xUzg7CQ5h2JlIb06ASNlQSOVQdsqw%3D%3D"
service_key_decoded =requests.utils.unquote(service_key)
req_parameter ={"ServiceKey":service_key_decoded,"searchSe":"road","srchwrd":"반포대로 201"}
result =requests.get(url,params=req_parameter)
print(result.text)

import xmltodict
dict_data = xmltodict.parse(result.text)
print(dict_data)
>>>>>>> 95108046ad14d562d3e70748b8ca18f27289bf62
print(dict_data['NewAddressListResponse']['newAddressListAreaCd']['zipNo'])
import requests
import json

BASE_URL = "https://connect.eiris.in"
data = {"userid": "manish@hubbler.mobi", "pswd": "hubbler@2017", "timezone": "Asia/Calcutta"}
s = requests.session()
response = s.post(BASE_URL + "/sessions/login/", json=data)
# print(response.json())
# print(s.headers)
# print(s.cookies["csrftoken2"])
# s.headers
# r = s.get(BASE_URL + "/otp/list")
# print(r.json())
# r = s.post(BASE_URL+"/validate-mobile/",json={"mobile":"1111100098"})
# print(r.json())
r = s.post(BASE_URL+"/rest/designations/",json={"name":"designation22"})
print(r.json())
r = s.delete(BASE_URL+"/rest/designations/"+r.json()["result"]["_id"])
print(r.json())
# print(r.json())

data ={
    "alias":"",
    "country_code":"IN",
    "departments":[],
    "designations":[],
    "dob":"",
    "doj":"",
    "email":"sdfg@sdgf.dfg",
"employee_id":"",
"firstname":"rem",
"gender":"",
"homephone":"null",
"lastname":"tes",
"mobile":"1111100003",
"mobile_country_code":{
    "international_dialing": "91",
    "country_name": "India",
    "country_code": "IN"},
"country_code":"IN",
"country_name":"India",
"international_dialing":"91",
"_id":"59880a4e13fd8efe651edc0d",
"officephone":"null",
"workaddress":{
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": ""},
    "address1":"",
    "address2":"",
    "city":"",
    "country":"",
    "state":"",
    "workphone":"null"
}

response = s.post(BASE_URL + "/rest/users/", json=data)
print(response.json())
r = s.post(BASE_URL+"/sessions/logout")
print(r.json())
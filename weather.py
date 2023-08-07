import requests



print("Hlow!")
print("This website helps you to know your city temperture.")

city_input=input("enter your city:")
api_key="8cdd30a10d72208e3a00cd4cbcbfbd0c"

def get_weather(api_key,city):
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response=requests.get(url).json()
    temp=response['main']['temp']
    city_temp=temp-273.15
    celcius=format(city_temp,".2f")
    print("the temperature in " + city + " is " +str(celcius)+"°C")


try:
    get_weather(api_key,city_input)

except:
    print("Invalid City Name")


import requests

url = "http://localhost:9696/predict"
# url = "fly_url"

water_sample0 = {
    "ph": 5.5,
    "hardness": 207,
    "solids": 44612,
    "chloramines": 7.0,
    "sulfate": 300,
    "conductivity": 553,
    "organic_carbon": 10,
    "trihalomethanes": 50,
    "turbidity": 3
}

water_sample1 = {
    "ph": 8.3,
    "hardness": 183.6,
    "solids": 20316,
    "chloramines": 7.0,
    "sulfate": 322,
    "conductivity": 295,
    "organic_carbon": 13,
    "trihalomethanes": 62.4,
    "turbidity": 4.2
}

if __name__ == "__main__":
    response = requests.post(url, json=water_sample1)
    predictions = response.json()
    if predictions["potability"]:
        print("Water is Potable")
    else:
        print("Water is not Potable")

# curl -X 'POST' \
#   'http://0.0.0.0:9696/predict' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "ph": 8.3,
#     "hardness": 183.6,
#     "solids": 20316,
#     "chloramines": 7.0,
#     "sulfate": 322,
#     "conductivity": 295,
#     "organic_carbon": 13,
#     "trihalomethanes": 62.4,
#     "turbidity": 4.2
# }'
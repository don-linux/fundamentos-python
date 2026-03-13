cafe = {
    "grano": "geisha",
    "pais": "colombia",
    "año": 2025,
}

print(cafe)
print(cafe["pais"])
print(cafe.get("grano"))
print(cafe.keys())
print(cafe.values())

if "grano" in cafe:
    print('Si hay!')

cafe["año"] = 2020

print(cafe)

cafe["tostado"] = "Suave"
print(cafe)

cafe.update({"año": 2022})
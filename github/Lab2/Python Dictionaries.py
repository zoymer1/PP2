car_info = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2020
}
print(car_info)

phone_spec = {
  "brand": "Samsung",
  "model": "Galaxy S21",
  "year": 2021
}
print(phone_spec["model"])

laptop_spec = {
  "brand": "Dell",
  "model": "XPS 13",
  "year": 2019
}
x = laptop_spec.get("model")
print(x)

book_details = {
  "title": "1984",
  "author": "George Orwell",
  "year": 1949
}
x1 = book_details.keys()
print(x1)

movie_info = {
  "title": "Inception",
  "director": "Christopher Nolan",
  "year": 2010
}
x2 = movie_info.values()
print(x2)

game_info = {
  "title": "The Witcher 3",
  "developer": "CD Projekt Red",
  "year": 2015
}
x3 = game_info.items()
print(x3)

city_info = {
  "name": "New York",
  "country": "USA",
  "population": 8419000
}
if "country" in city_info:
  print("Yes, 'country' is a key in city_info")

person_info = {
  "name": "Alice",
  "age": 25,
  "city": "Berlin"
}
person_info["age"] = 26
print(person_info)

student_info = {
  "name": "John",
  "age": 21,
  "university": "Harvard"
}
student_info["grade"] = "A"
print(student_info)

pet_info = {
  "name": "Buddy",
  "species": "Dog",
  "age": 5
}
pet_info.update({"color": "Brown"})
print(pet_info)

car_spec = {
  "brand": "BMW",
  "model": "X5",
  "year": 2022
}
car_spec.pop("model")
print(car_spec)

fruit_info = {
  "name": "Apple",
  "color": "Red",
  "taste": "Sweet"
}
fruit_info.popitem()
print(fruit_info)

laptop_info = {
  "brand": "HP",
  "model": "Pavilion",
  "year": 2021
}
del laptop_info["model"]
print(laptop_info)

sports_info = {
  "name": "Football",
  "players": 11,
  "origin": "England"
}
sports_info.clear()
print(sports_info)

company_info = {
  "name": "Tesla",
  "CEO": "Elon Musk",
  "founded": 2003
}
for x4 in company_info:
  print(x4)

  country_info = {
  "name": "Japan",
  "capital": "Tokyo",
  "population": 126300000
}
for x5 in country_info.values():
  print(x5)

university_info = {
  "name": "MIT",
  "location": "USA",
  "ranking": 1
}
for x6 in university_info.keys():
  print(x6)

bike_info = {
  "brand": "Yamaha",
  "model": "YZF-R1",
  "year": 2022
}
for x7, y7 in bike_info.items():
  print(x7, y7)

watch_info = {
  "brand": "Rolex",
  "model": "Submariner",
  "year": 2020
}
new_watch_info = watch_info.copy()
print(new_watch_info)

tablet_info = {
  "brand": "Apple",
  "model": "iPad Pro",
  "year": 2021
}
new_tablet_info = dict(tablet_info)
print(new_tablet_info)

family_info = {
  "parent1": {
    "name": "Robert",
    "age": 45
  },
  "parent2": {
    "name": "Julia",
    "age": 42
  },
  "child": {
    "name": "Lucas",
    "age": 18
  }
}
print(family_info)


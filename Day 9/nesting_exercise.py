travel_log1 = [
    {
    "Country":"Nepal", 
    "cities_visited": ["Kathmandu", "Pokhara", "Chitwan"], 
     "Total_visited": 3
     },
     {
    "Country":"India",
    "city_visit":["Goa", "Darjaling", "Sikkham",], 
    "Total_visit":2 
    }
]
def add_new_country(country_name, cities_visit, total_visit):
    new_country ={}
    new_country["country"] = country_name
    new_country["cities_visited"] = cities_visit
    new_country["Total_visited"] = total_visit
    travel_log1.append(new_country)
add_new_country("France",["Paris","lille", "Dijon"],2)  
print(travel_log1)
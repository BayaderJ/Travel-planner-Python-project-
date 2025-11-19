import data
import random

def getting_destination(budget, trip_types):
    #Creating 2 list to provide the user with global and local recommendations
    global_recommendations = []
    local_recommendations = []

    #Convert all trip type names to lowercase for easy matching using lambda
    trip_types = list(map(lambda t: t.lower(), trip_types))

    """
    Doing iteration over both travel dictionaries (global & local)
    to find:
        - destinations matching the user budget with a -100 SAR tolerance
        - destinations matching any of the chosen trip types
    """
    for des_name, des_info in data.travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        price_diff = budget - avg_price
        trip_type_list = des_info["trip_type"]
        if 0 <= price_diff <= 100 and any(t in trip_type_list for t in trip_types):
            global_recommendations.append({des_name: des_info})

    for des_name, des_info in data.saudi_travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        price_diff = budget - avg_price
        trip_type_list = des_info["trip_type"]
        if 0 <= price_diff <= 100 and any(t in trip_type_list for t in trip_types):
            local_recommendations.append({des_name: des_info})
    #Creating a varibale to store any type that doesn't have a matching budget in our data
    missing_types = []
    any_found = False

    # Using if, elif, else to filter the trip type for each type recommendation
    for t in trip_types:
        global_filtered = [
            rec for rec in global_recommendations
            if t in list(rec.values())[0]["trip_type"]
        ]
        local_filtered = [
            rec for rec in local_recommendations
            if t in list(rec.values())[0]["trip_type"]
        ]

        if global_filtered or local_filtered:
            any_found = True
            print(f"\nRecommendations for {t} trip:")

        if global_filtered and local_filtered:
            print_recommendations(" Global Recommendations", global_filtered)
            print_recommendations(" Local Recommendations", local_filtered)
        elif global_filtered:
            print_recommendations(" Global Recommendations", global_filtered)
        elif local_filtered:
            print_recommendations(" Local Recommendations", local_filtered)
        else:
            missing_types.append(t)

    if missing_types:
        print("\nSorry! No recommendation matches your preferences and budget for:",end="")
        print(" " + ", ".join(missing_types))
        print("Try adjusting your budget or choosing different trip types\n")

#Defining a printing function for better readability
def print_recommendations(title, recs):
    print(f"\n{title}:")
    if recs:
        rec = random.choice(recs)
        for name, info in rec.items():
            print(f"\n Destination: {name}")
            if "country" in info:
                print(f" Country: {info['country']}")
            else:
                print(f" Region: {info['region']}")
            print(f" Avg Budget/Day: {info['average_budget_per_day']} SAR")
            print(" Activities:")
            for act in info['activities']:
                print(f"   - {act}")
            print()
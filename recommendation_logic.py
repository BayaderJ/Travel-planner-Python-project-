
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
        if 0 <= price_diff <= 100:
            if any(t in des_info["trip_type"] for t in trip_types):
                global_recommendations.append({des_name: des_info})

    for des_name, des_info in data.saudi_travel_data.items():
        avg_price = des_info["average_budget_per_day"]
        price_diff = budget - avg_price
        if 0 <= price_diff <= 100:
            if any(t in des_info["trip_type"] for t in trip_types):
                local_recommendations.append({des_name: des_info})

    #printing logic using if, elif, and else
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


    for t in trip_types:
        selected = t

        global_filtered = [
            rec for rec in global_recommendations
            if selected in list(rec.values())[0]["trip_type"]
        ]
        local_filtered = [
            rec for rec in local_recommendations
            if selected in list(rec.values())[0]["trip_type"]
        ]

        if global_filtered or local_filtered:
            print(f"\nRecommendations for {selected} trip:")

        if global_filtered and local_filtered:
            print_recommendations(" Global Recommendations", global_filtered)
            print_recommendations(" Local Recommendations", local_filtered)
        elif global_filtered:
            print_recommendations(" Global Recommendations", global_filtered)
        elif local_filtered:
            print_recommendations(" Local Recommendations", local_filtered)
        else:
            print("\n Sorry! No recommendation matches your preferences and budget.")
            print("Try adjusting your budget or choosing different trip types\n")


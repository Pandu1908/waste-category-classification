waste = input("Enter waste item: ").lower()

organic = ["food", "banana", "apple", "vegetable", "leaves"]
recyclable = ["plastic bottle", "paper", "cardboard", "glass", "can"]
general = ["diaper", "thermocol", "used tissue"]

if waste in organic:
    print("🌱 Category: Organic Waste")
    print("Suggestion: Put it in the compost/organic waste bin.")

elif waste in recyclable:
    print("♻️ Category: Recyclable Waste")
    print("Suggestion: Send it for recycling.")

elif waste in general:
    print("🗑️ Category: General Waste")

else:
    print("Item not recognized.")

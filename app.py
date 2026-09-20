from flask import Flask, render_template, request
from rapidfuzz import process, fuzz

app = Flask(__name__)


def classify_waste(waste_item):

    item = waste_item.lower().strip()

    wet_waste = [
        "banana peel",
        "banana skin",
        "apple core",
        "orange peel",
        "orange skin",
        "mango peel",
        "mango seed",
        "vegetable",
        "vegetable waste",
        "vegetable scraps",
        "fruit",
        "fruit waste",
        "fruit scraps",
        "fruit seeds",
        "leftover food",
        "food",
        "food waste",
        "food scraps",
        "cooked food",
        "rice",
        "bread",
        "chapati",
        "roti",
        "tea leaves",
        "tea bag",
        "coffee grounds",
        "eggshell",
        "egg shell",
        "onion peel",
        "potato peel",
        "tomato waste",
        "carrot peel",
        "spoiled food",
        "meat waste",
        "fish waste",
        "chicken bones",
        "bones",
        "garden leaves",
        "leaves",
        "grass",
        "flowers",
        "plant waste",
        "weeds"
    ]

    dry_waste = [
        
        "paper",
        "newspaper",
        "magazine",
        "notebook",
        "book",
        "cloth bag",
        "fabric bag",
        "jute bag",
        "cotton bag",
        "cardboard",
        "carton",
        "paper bag",
        "paper cup",
        "paper plate",
        "tissue box",
        "paper wrapper",
        "plastic bottle",
        "water bottle",
        "plastic container",
        "plastic cup",
        "plastic box",
        "plastic bag",
        "polythene bag",
        "shopping bag",
        "plastic wrapper",
        "snack wrapper",
        "biscuit wrapper",
        "milk packet",
        "detergent bottle",
        "shampoo bottle",
        "soap box",
        "glass bottle",
        "glass jar",
        "metal can",
        "tin can",
        "aluminium can",
        "steel can",
        "pen",
        "pencil",
        "marker",
        "toothpaste box",
        "packaging box",
        "empty box",
        "plastic",
        "glass",
        "metal"
    ]

    hazardous_waste = [
        "battery",
        "batteries",
        "used battery",
        "medicine",
        "expired medicine",
        "medical waste",
        "syringe",
        "injection needle",
        "needle",
        "thermometer",
        "paint",
        "paint can",
        "pesticide",
        "insecticide",
        "chemical waste",
        "cleaning chemical",
        "bleach bottle",
        "disinfectant chemical",
        "used bandage"
    ]

    electronic_waste = [
        "mobile phone",
        "smartphone",
        "cellphone",
        "tablet",
        "charger",
        "charging cable",
        "usb cable",
        "cable",
        "earphones",
        "headphones",
        "computer",
        "laptop",
        "keyboard",
        "mouse",
        "computer mouse",
        "printer",
        "printer cartridge",
        "calculator",
        "remote control",
        "power bank",
        "electric wire",
        "electronic device",
        "e-waste",
        "led bulb",
        "electronic toy"
    ]
    all_waste_items = (
        wet_waste
        + dry_waste
        + hazardous_waste
        + electronic_waste
    )

    match = process.extractOne(
        item,
        all_waste_items,
        scorer=fuzz.WRatio
    )

    if match and match[1] >= 70:
        item = match[0]

    # Check more specific categories first
    
    if any(word in item for word in hazardous_waste):
        return {
            "category": "Hazardous Waste",
            "disposal": "Do not mix it with regular household waste. Use an appropriate hazardous-waste collection facility.",
            "tip": "Proper handling of hazardous waste helps protect people and the environment.",
            "confidence": "High"
        }

    elif any(word in item for word in electronic_waste):
        return {
            "category": "E-Waste",
            "disposal": "Give electronic waste to an authorized e-waste collection or recycling facility.",
            "tip": "Responsible e-waste recycling helps recover valuable materials and reduces environmental harm.",
            "confidence": "High"
        }

    elif any(word in item for word in wet_waste):
        return {
            "category": "Wet / Organic Waste",
            "disposal": "Place it in the appropriate wet-waste or composting system.",
            "tip": "Composting organic waste can help reduce the amount of waste sent to landfills.",
            "confidence": "High"
        }

    elif any(word in item for word in dry_waste):
        return {
            "category": "Dry / Recyclable Waste",
            "disposal": "Place it in the appropriate dry-waste or recycling collection system.",
            "tip": "Cleaning and properly segregating recyclable materials can support recycling.",
            "confidence": "High"
        }

    else:
        return {
            "category": "Unknown",
            "disposal": "The item could not be confidently classified. Please describe the material, such as plastic, paper, glass, metal, or organic.",
            "tip": "Correct identification helps ensure responsible waste segregation.",
            "confidence": "Low"
        }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        waste_item = request.form.get("waste_item", "").strip()

        if waste_item:

            classification = classify_waste(waste_item)

            result = {
                "item": waste_item,
                "category": classification["category"],
                "disposal": classification["disposal"],
                "tip": classification["tip"],
                "confidence": classification["confidence"]
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
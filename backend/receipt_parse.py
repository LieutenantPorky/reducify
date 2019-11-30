from fuzzywuzzy import fuzz

def filter(name, choices, cutoff=70):
    current_max = 0
    current_choice = ""
    for i in choices:
        match = fuzz.ratio(name, i)
        if match >= cutoff and match > current_max:
            current_choice = i
            current_max = match
    if current_max >= cutoff:
        return current_choice
    return None



if __name__ == "__main__":
    choices = ["garlic", "tomatoes", "turkey", "potatoes"]
    input = ["gallic", "tomatoes", "blueberries"]
    print([filter(i,choices,70) for i in input])

# Let´s define our function
def listingTerms(**kwargs):  # kwargs can accept key-value (dictionary) terms
    # Let´s i-terate every element in our kwargs argument
    for key, value in kwargs.items():  # We use the .items method in order to return a new view of the Dictionary Items
        print(f"{key}:{value}")  # Let's print our f-string output


listingTerms(IDE="Integrated Development Environment", API="Application Program Interface")

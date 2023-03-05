def listingTerms(**kwargs):  # kwargs can accept key-value (dictionary) terms
    for key, value in kwargs.items():  #
        print(f"{key}:{value}")


listingTerms(IDE="Integrated Development Environment", API="Application Program Interface")

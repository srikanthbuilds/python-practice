def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_address(country = "US",state = "detriot",city = "california")

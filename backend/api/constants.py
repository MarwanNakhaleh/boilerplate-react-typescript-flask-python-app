from pydoc import locate

args_dict = {
    "min_bedrooms": locate("int"),
    "max_bedrooms": locate("int"),
    "min_bathrooms": locate("int"),
    "max_bathrooms": locate("int"),
    "min_price": locate("float"),
    "max_price": locate("float"),
    "start": locate("int"),
    "limit": locate("int"),
    "city": locate("str"),
    "state": locate("str"),
    "is_test": locate("str")
}
def combinar_strings(string1, string2):
    if len(string1) > 2 and len(string2) > 2:
        return string1[:2] + string2[-2:]
    else:
        return "Los strings deben tener una longitud mayor a 2"


result = combinar_strings("familia", "abrigarse")
print(result)

def comma_sep(names: list[str]) -> str:
    output = str()

    for x in range(len(names)):
        if output:
            if x == len(names) - 1:
                output += ' and '
            else:
                output += ', '
        output += names[x]

    return output


print(comma_sep([]))
print(comma_sep(["Daniel"]))
print(comma_sep(["Daniel", "Johnny"]))
print(comma_sep(["Daniel", "Johnny", "Mike"]))

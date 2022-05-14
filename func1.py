def get_summ(one, two, delimiter='&'):
    return str(one) + delimiter + str(two)


a = get_summ("Learn", 'Python')
print(a.upper())
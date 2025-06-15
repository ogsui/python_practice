is_male = True
is_tall = True

if is_male and is_tall:
    print("you are male and tall")
elif is_male and not(is_tall):
    print("you are short male")
elif not(is_male) and is_tall:
    print("you are a tall girl")
else:
    print("you are female nor tall")
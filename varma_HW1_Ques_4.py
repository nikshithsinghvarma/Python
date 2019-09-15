# Nikshith Singh Varma
# 1001667758
#
# To print a Celsius to Fahrenhite conversion table
print("\t_________________\t")
print("\t|___C___|____F___|\t")
for c in range(0, 21):
    f = float((9/5)*c) + 32
    if c < 10:
        print("\t|  ", c, "  | ", format(f, ".2f"), "|\t")
    else:
        print("\t| ", c, "  | ", format(f, ".2f"), " |\t")
print("\t_________________\t")

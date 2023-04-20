from toolbox import ArbreB_Huffmann, Sommet

abr1 = ArbreB_Huffmann.build_from_text("ceci est un test", True)
abr2 = ArbreB_Huffmann.build_from_text("ok je dors", True)
print(abr1)
print(abr2)
abr3 = abr1 + abr2
print(abr3)
abr3 -= "t"
print(abr3)
abr3 += Sommet(12, "e")
print(abr3)
abr3 -= "e"
print(abr3)
abr4, abr5 = abr3.decomposition()
print(abr4)
print(abr5)
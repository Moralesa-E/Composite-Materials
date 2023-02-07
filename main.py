
from list_of_compunds import ListofCompounds

from material import Material
from materials_list import MaterialsList

if __name__=="__main__":


    e1 = Material("Fibra", "Vidrio", 85.01, 0.2, 35.41, 1.543, 1.543)
    e2 = Material("Fibra", "Aramida", 123.97, 0.36, 2.99, -1.543, 1.265)
    e3 = Material("Matriz", "Epoxica", 3.39, 0.3, 1.31, 19.44, 19.44, 0.33)
    e4 = Material("Matriz", "Poliamida", 3.39, 0.35, 1.299, 27.77, 27.77, 0.33)

    le1 = MaterialsList()

    le1.add_material(e1)
    le1.add_material(e2)
    le1.add_material(e3)
    le1.add_material(e4)

    le1.show_list()

    c1 = le1.create_compound(id_f=0,id_m=2)
    c1.add_elast_const(0.5,0.5)
    c2 = le1.create_compound(id_f=0,id_m=3)
    c2.add_elast_const(0.5,0.5)

    lc1 = ListofCompounds()

    lc1.add(c1)
    lc1.add(c2)

    lc1.show_list()
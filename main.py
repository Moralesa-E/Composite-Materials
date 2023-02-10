
from materials.list_of_compunds import ListofCompounds

from materials.fiber import Fiber
from materials.matrix import Matrix
from materials.materials_list import MaterialsList

if __name__=="__main__":


    e1 = Fiber("Vidrio", 85.01, 0.2, 35.41, 1.543, 1.543)
    e2 = Fiber("Aramida", 123.97, 0.36, 2.99, -1.543, 1.265)
    e3 = Matrix("Epoxica", 3.39, 0.3, 1.31, 19.44, 19.44, 0.33)
    e4 = Matrix("Poliamida", 3.39, 0.35, 1.299, 27.77, 27.77, 0.33)

    le1 = MaterialsList()

    le1.add_material(e1)
    le1.add_material(e2)
    le1.add_material(e3)
    le1.add_material(e4)

    le1.show_list()

    c1 = le1.create_compound(id_f=0,id_m=2,vf=0.5,vm=0.5,)
    c1.calc_elast_const()
    c1.calc_sxy(theta=55)
    c2 = le1.create_compound(id_f=0,id_m=3,vf=0.5,vm=0.5)
    c2.calc_elast_const()

    lc1 = ListofCompounds()

    lc1.add(c1)
    lc1.add(c2)

    lc1.show_list()
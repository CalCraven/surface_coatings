import mbuild as mb
from mbuild.lib.recipes import Polymer
import numpy as np

from surface_coatings.monomers import MethylStyrene
from surface_coatings.monomers import (AzPMA, SBMA, Methacrylate, TriazoleBiotin)


class VBCPolymer(mb.Compound):
    def __init__(self, monomers=[Methacrylate(), SBMA(), AzPMA(), TriazoleBiotin()], n=1,
                 sequence='AABCBBD', port_labels=('up', 'down')):
        super(VBCPolymer, self).__init__()
        copolymer = Polymer(monomers=monomers)
        copolymer.build(n=n, sequence=sequence, add_hydrogens=False)
        self.add(copolymer)
        vbc = MethylStyrene()
        self.add(vbc)
        mb.force_overlap(vbc,
                         vbc['up'],
                         copolymer['up'])
        for port in self.all_ports():
            if port.access_labels:
                self.labels['up'] = port
            else:
                self.labels['down'] = port

        orientation = self['Polymer[0]']['down'].direction
        for port in self.available_ports():
            if not all(np.isclose(port.direction, orientation)):
                port.update_orientation(-orientation)

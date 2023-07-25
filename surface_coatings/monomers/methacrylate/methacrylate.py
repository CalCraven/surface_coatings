"""Methacrylate monomer class."""
import mbuild as mb
from mbuild.lib.atoms import H
from mbuild.lib.moieties import CH2, CH3


class Methacrylate(mb.Compound):
    """Methacrylate monomer.

    Parameters
    ----------
    front_cap : bool, optional, default=False
        Add hydrogen cap to the front end of the Methacrylate. To be implemented.
    rear_cap : bool, optional, default=False
        Add hydrogen cap to the rear end of the Methacrylate. To be implemented.
    """

    def __init__(self, front_cap=False, rear_cap=False):
        super(Methacrylate, self).__init__()
        # self.add(mb.load('CC(=C)C(=O)O', smiles=True))
        mb.load(
            "methacrylate.mol2",
            compound=self,
            relative_to_module=self.__module__,
            backend="gmso",
            infer_hierarchy=False,
        )
        self.translate(-self[1].pos)
        bond_vect = self[1].pos - self[2].pos
        self.add(
            mb.Port(anchor=self[1], orientation=bond_vect, separation=0.07),
            "up",
        )
        self.add(
            mb.Port(anchor=self[2], orientation=bond_vect, separation=-0.07),
            "down",
        )
        if front_cap:
            hydrogen = H()
            # TODO call forceoverlap
        if rear_cap:
            hydrogen = H()
            # TODO call forceoverlap


if __name__ == "__main__":
    compound = Methacrylate()
    print(compound)

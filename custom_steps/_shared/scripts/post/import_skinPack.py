# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp
from mgear.core import skin
import os


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "import_skinPack"

    def run(self, stepDict):
        """Run method.

            i.e:  stepDict["mgearRun"].global_ctl  gets the global_ctl from
                    shifter rig on post step
            i.e:  stepDict["otherCustomStepName"].ctlMesh  gets the ctlMesh
                    from a previous custom step called "otherCustomStepName"
        Arguments:
            stepDict (dict): Dictionary containing the objects from
                the previous steps

        Returns:
            None: None
        """
        skinPack = os.path.join(
            stepDict["paths"].data_path, "skin", "skin.gSkinPack")
        skin.importSkinPack(skinPack)

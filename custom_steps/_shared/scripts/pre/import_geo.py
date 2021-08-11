# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp


import os

import pymel.core as pm

import mgear.shifter.custom_step as cstp


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "import_geo"

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

        path = os.sep.join([stepDict["paths"].asset_path,
                            "geo.ma"])
        print(path)

        pm.importFile(path)

        try:
            pm.select("guide")
        except pm.MayaNodeError:
            pass

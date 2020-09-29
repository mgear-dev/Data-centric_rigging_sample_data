# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp
import os
import maya.mel as mel
import pymel.core as pm


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "import_SHAPES"

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

        if not pm.pluginInfo("weightDriver", q=True, loaded=True):
            try:
                pm.loadPlugin("weightDriver")
            except RuntimeError:
                pm.displayError("You need the weightDriver plugin!")
                raise

        self.importSHAPES(stepDict, "body_blendShape")

    def importSHAPES(self, stepDict, fileName):
        shapesMelFile = os.path.join(
            stepDict["paths"].asset_base_path,
            "_shared",
            "data",
            "SHAPES",
            "{}.mel".format(fileName))
        shapesMelFile = shapesMelFile.replace("\\", "/")

        mel.eval('source "%s";' % shapesMelFile)

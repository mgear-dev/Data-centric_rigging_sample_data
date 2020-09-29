# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp

# maya
import pymel.core as pm


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "init_base"

    def run(self, stepDict):
        self.load_cvwrap()
        self.modelName = stepDict["mgearRun"].model.name()
        self.controllers_grp = pm.PyNode(self.modelName + "_controllers_grp")
        self.deformers_grp = pm.PyNode(self.modelName + "_deformers_grp")
        self.staticJnt(stepDict)
        self.initialStructure(stepDict)

    def initialStructure(self, stepDict):
        # setting objects
        self.geo_root = pm.PyNode("geo_root")

        # set the preview smooth division to 0
        ts = self.geo_root.getChildren(allDescendents=True)
        pm.displaySmoothness(ts, polygonObject=0)

        self.facial_local_setups = pm.createNode(
            "transform",
            name="facial_local_setup",
            p=stepDict["mgearRun"].setupWS)

        # reparent geo root
        pm.parent(self.geo_root, stepDict["mgearRun"].model)

    def staticJnt(self, stepDict):
        try:
            jnt_parent = stepDict["mgearRun"].jnt_org
        except AttributeError:
            jnt_parent = stepDict["mgearRun"].setupWS
        self.staticJnt = pm.createNode("joint",
                                       name="static_jnt",
                                       p=jnt_parent)

        self.deformers_grp.add(self.staticJnt)

    def load_cvwrap(self):
        # wrap face to head rig
        try:
            if not pm.pluginInfo("cvwrap", q=True, loaded=True):
                pm.loadPlugin("cvwrap")
                pm.displayInfo("cvrap plugin loaded!")
        except RuntimeError:
            pm.displayError("You need the cvWrap plugin!")
            raise

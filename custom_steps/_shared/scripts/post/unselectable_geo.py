# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp


import mgear.shifter.custom_step as cstp
from mgear.core import attribute
import pymel.core as pm


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "unselectable_geo"

    def run(self, stepDict):

        root = stepDict["mgearRun"].model
        geo_root = stepDict["init_base"].geo_root

        attribute.addAttribute(root, "geoUnselectable", "bool", True)

        pm.connectAttr(root.geoUnselectable, geo_root.attr("overrideEnabled"))
        geo_root.attr("overrideDisplayType").set(2)

# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp

# maya
import pymel.core as pm

BEFORE = r"""
import mgear.core.callbackManager as cb
import pymel.core as pm
from mgear.core  import transform

def swap_proxyCtl_selection(*args):
    if pm.selected():
        osel =  pm.selected()[0]
        if "UIproxy" in osel.name():
            ctl = osel.name().replace("UIproxy", "UI")


            try:
                pm.select(ctl)
            except pm.MayaNodeError:
                pm.displayWarning("Swap control Can't find {}".format(osel.name()))

swap_proxyCtl_cb_manager = cb.CallbackManager()
swap_proxyCtl_cb_manager.selectionChangedCB("swap_proxyCtl_cb",
                                             swap_proxyCtl_selection)

"""

AFTER = r"""
swap_proxyCtl_cb_manager.removeAllManagedCB()
"""


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "proxy_ctl_swap_callback"

    def run(self, stepDict):

        self.cb_node = pm.scriptNode(st=1,
                                     beforeScript=BEFORE,
                                     afterScript=AFTER,
                                     n='swap_proxyCtl_cb_node',
                                     stp='python')
        pm.scriptNode(self.cb_node, executeBefore=True)

        self.connections(stepDict)

    def connections(self, stepDict):
        # TODO: create connectNextAvailable cfunction
        i = 0
        while True:
            try:
                pm.connectAttr(
                    pm.PyNode(self.cb_node).message,
                    stepDict["mgearRun"].model.attr(
                        "rigScriptNodes[%s]" % str(i)))
                break
            except:
                i += 1
                if i > 100:
                    pm.displayWarning("next available reached limit 100")
                    break

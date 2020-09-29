# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp
import pymel.core as pm


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "channel_default_values_config"

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
        stepDict["mgearRun"].model.jnt_vis.set(0)
        # rootName = stepDict["mgearRun"].model.name()
        try:
            pm.setAttr("spineUI_C0_ctl.neck_volume", 0)
            pm.setAttr("spineUI_C0_ctl.spine_volume", 0)

            pm.setAttr("armUI_L0_ctl.arm_volume", 0)
            pm.setAttr("armUI_R0_ctl.arm_volume", 0)

            pm.setAttr("legUI_L0_ctl.leg_volume", 0)
            pm.setAttr("legUI_R0_ctl.leg_volume", 0)

            pm.setAttr("setup_geoRoot.visibility", False)
        except:
            pass

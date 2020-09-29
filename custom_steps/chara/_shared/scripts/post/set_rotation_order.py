# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp
import pymel.core as pm


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "set_rotation_order"

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
        pm.setAttr("neck_C0_head_ctl.rotateOrder", 3)
        pm.setAttr("neck_C0_ik_ctl.rotateOrder", 3)
        pm.setAttr("spine_C0_ik0_ctl.rotateOrder", 3)
        pm.setAttr("body_C0_ctl.rotateOrder", 3)
        pm.setAttr("arm_L0_fk0_ctl.rotateOrder", 2)
        pm.setAttr("arm_R0_fk0_ctl.rotateOrder", 2)
        pm.setAttr("leg_L0_fk2_ctl.rotateOrder", 3)
        pm.setAttr("leg_R0_fk2_ctl.rotateOrder", 3)

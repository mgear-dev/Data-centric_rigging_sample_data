# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp



import mgear.shifter.custom_step as cstp
from mgear.core import transform


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "reset_hand_IK"

    def run(self, stepDict):
        """Run method.

            i.e:  stepDict["mgearRun"].global_ctl  gets the global_ctl from
                    shifter rig on post step
            i.e:  stepDict["otherCustomStepName"].ctlMesh  gets the
                    ctlMesh from a previous custom
                    step called "otherCustomStepName"
        Args:
            stepDict (dic): Dictionary containing the objects from the
            previous steps

        Returns:
            None: None
        """
        for side in "LR":
            handIK_ctl = stepDict["mgearRun"].components["arm_{}0".format(side)].ik_ctl
            transform.resetTransform(handIK_ctl)

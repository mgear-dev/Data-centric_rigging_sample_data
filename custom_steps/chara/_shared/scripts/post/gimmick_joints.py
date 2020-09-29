# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp

from mgear import rigbits
import pymel.core as pm


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "gimmick_joints"

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
        self.model_name = stepDict["mgearRun"].model.name()
        self.create_gimmick()

    def create_gimmick(self):

        fingers = []
        for i in "0123":
            for e in "012":
                fingers.append("finger_L{}_{}_jnt".format(i, e))

        for e in "012":
            fingers.append("thumb_L0_{}_jnt".format(e))

        jntList = ["arm_L0_end_jnt",
                   "leg_L0_0_jnt",
                   "leg_L0_3_jnt",
                   "arm_L0_0_jnt",
                   "arm_L0_3_jnt"]

        for side in "LR":
            for jname in jntList + fingers:
                sJnt = pm.PyNode(jname.replace("L", side))
                rigbits.addBlendedJoint(sJnt)

        self.defSet = pm.PyNode(self.model_name + "_deformers_grp")
        deform = pm.PyNode("rig_deformers_grp")
        self.defSet.addMembers(
            [m for m in deform.members() if m.type() == "joint"])
        pm.delete("rig_deformers_grp")

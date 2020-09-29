# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import os


import mgear.shifter.custom_step as cstp


# CUSTOM_STEPS_DIR = os.environ.get('MGEAR_SHIFTER_CUSTOMSTEP_PATH', None)
# os.sys.path.append(CUSTOM_STEPS_DIR)


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "paths"

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

        asset_relative_path = __file__.rpartition('custom_steps' + os.sep)[2]
        path_part = asset_relative_path.split(os.sep)

        self.asset_type = path_part[0]
        self.asset_name = path_part[1]
        self.asset_variant = path_part[2]
        self.asset_target = path_part[3]

        self.custom_steps_path = os.sep.join(os.path.abspath(
            os.path.dirname(__file__)).split(os.sep)[:-2])

        self.asset_base_path = os.sep.join(os.path.abspath(
            os.path.dirname(__file__)).split(os.sep)[:-4])

        self.variant_base_path = os.sep.join(os.path.abspath(
            os.path.dirname(__file__)).split(os.sep)[:-3])

        self.custom_steps_base_path = os.sep.join(os.path.abspath(
            os.path.dirname(__file__)).split(os.sep)[:-6])

        self.asset_path = os.sep.join([self.custom_steps_path, "assets"])
        self.data_path = os.sep.join([self.custom_steps_path, "data"])
        self.pre_scripts_path = os.sep.join(
            [self.custom_steps_path, "scripts", "pre"])
        self.post_scripts_path = os.sep.join(
            [self.custom_steps_path, "scripts", "post"])

        print "asset_type: " + self.asset_type
        print "asset_name: " + self.asset_name
        print "asset_target: " + self.asset_target
        print "custom_steps_path: " + self.custom_steps_path
        print "custom_steps_base_path: " + self.custom_steps_base_path
        print "asset_path: " + self.asset_path
        print "data_path: " + self.data_path
        print "pre_scripts_path: " + self.pre_scripts_path
        print "post_scripts_path: " + self.post_scripts_path
        print "asset_base_path: " + self.asset_base_path
        print "variant_base_path: " + self.variant_base_path

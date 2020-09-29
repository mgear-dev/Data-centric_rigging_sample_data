# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp
from mgear.anim_picker import picker_node
from mgear.anim_picker.handlers import file_handlers
import pymel.core as pm
import os


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "anim_picker"

    def run(self, stepDict):
        """Run method.

            i.e:  stepDict["mgearRun"].global_ctl  gets the global_ctl from
                    shifter rig build bas
            i.e:  stepDict["mgearRun"].components["control_C0"].ctl  gets the
                    ctl from shifter component called control_C0
            i.e:  stepDict["otherCustomStepName"].ctlMesh  gets the ctlMesh
                    from a previous custom step called "otherCustomStepName"
        Arguments:
            stepDict (dict): Dictionary containing the objects from
                the previous steps

        Returns:
            None: None
        """

        file_path = os.path.join(stepDict["paths"].custom_steps_base_path,
                                 "chara",
                                 "_shared",
                                 "data",
                                 "biped.pkr")
        pkr_data = file_handlers.read_data_file(file_path)
        node = picker_node.DataNode()
        node.create()
        node.write_data(data=pkr_data)
        node.read_data()
        pm.parent(node, "rig")
        pm.setAttr("PICKER_DATAS.picker_datas_file", file_path, type="string")
        pm.rename(node, "PICKER_DATA_BIPED")

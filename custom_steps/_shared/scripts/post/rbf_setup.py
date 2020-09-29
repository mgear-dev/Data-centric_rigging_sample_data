# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

import mgear.shifter.custom_step as cstp

from mgear.rigbits import rbf_io
import os


class CustomShifterStep(cstp.customShifterMainStep):

    def __init__(self):
        self.name = "rbf_setup"

    def run(self, stepDict):

        rbfPath = os.path.join(stepDict["paths"].asset_base_path,
                               "_shared",
                               "data",
                               "rbf.rbf")
        rbf_io.importRBFs(rbfPath)

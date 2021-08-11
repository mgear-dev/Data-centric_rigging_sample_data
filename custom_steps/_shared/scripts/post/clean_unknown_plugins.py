# Data-Centric rigging 2020 Sample Data
# www.studioanima.co.jp

from pprint import pprint

import maya.cmds as mc

unknownPlugins = mc.unknownPlugin(q=True, list=True) or []
for pl in unknownPlugins:
    # force removal of plugins
    mc.unknownPlugin(pl, remove=True)

print("The following unknown plugins removed!")
pprint(unknownPlugins)

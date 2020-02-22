# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *


from poco.drivers.unity3d import UnityPoco

from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False,force_restart=False)





# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)



for i in range(1000):
    exit_btn =  poco(text="重播")
    exit_btn.wait_for_appearance(timeout=1200)
    next_btn = poco(text="下一篇")
    next_btn.click()
     




















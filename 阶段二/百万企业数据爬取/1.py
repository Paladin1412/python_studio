# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿

import re
str ="485 / 115 = "
data = re.findall('\/ ([0-9]+)',str)
print(data)
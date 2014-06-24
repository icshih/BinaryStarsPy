#!/usr/bin/env python

import bs.common.twoBody as tb

test = tb.twoBody(1.0, 5.0, 20.0)
print(test.getDistanceToMassOne(), test.getDistanceToMassTwo())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for photometers manufactured by Gamma Sci
"""

# Originally from the PsychoPy library
# Copyright (C) 2002-2018 Jonathan Peirce (C) 2019-2022 Open Science Tools Ltd.
# Distributed under the terms of the GNU General Public License (GPL).

from psychopy import hardware, plugins


from psychopy_gammasci.gammasci import S470

plugins.activatePlugins()


def test_getPhotometers():
    """
    Test that Gamma Sci photometers appear in getAllPhotometers once plugins are activated
    """
    # get all photometers
    photoms = hardware.getAllPhotometers()
    # make sure classes are present
    assert S470 in photoms

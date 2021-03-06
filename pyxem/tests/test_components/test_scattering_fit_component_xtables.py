# -*- coding: utf-8 -*-
# Copyright 2017-2019 The pyXem developers
#
# This file is part of pyXem.
#
# pyXem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyXem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyXem.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import numpy as np
from pyxem.signals.reduced_intensity1d import ReducedIntensity1D
from pyxem.components.scattering_fit_component_xtables import ScatteringFitComponentXTables


def test_scattering_component_init_xtables():
    ref = ScatteringFitComponentXTables(['Cu'], [1], N=1., C=0.)
    assert isinstance(ref, ScatteringFitComponentXTables)


@pytest.fixture(params=[
    np.array([4., 3., 2., 2., 1., 1., 1., 0.])
])
def ri_model(request):
    ri = ReducedIntensity1D(request.param)
    m = ri.create_model()
    return m


def test_function_xtables(ri_model):
    elements = ['Cu']
    fracs = [1]
    sc_component = ScatteringFitComponentXTables(elements, fracs, N=1., C=0.)
    ri_model.append(sc_component)
    ri_model.fit()

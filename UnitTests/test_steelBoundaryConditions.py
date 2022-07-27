import sys
import os
import pytest
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

# Import der Bibliotheken
from RFEM.enums import *
from RFEM.initModel import Model, SetAddonStatus, CheckIfMethodOrTypeExists
from RFEM.TypesForSteelDesign.steelBoundaryConditions import *

if Model.clientModel is None:
    Model()

@pytest.mark.skipif(CheckIfMethodOrTypeExists(Model.clientModel,'ns0:steel_boundary_conditions', True), reason="Type ns0:steel_boundary_conditions not in RFEM GM yet")

def test_steelEffectiveLengths():

    Model.clientModel.service.begin_modification()

    SetAddonStatus(Model.clientModel, AddOn.steel_design_active, True)

    SteelBoundaryConditions(1, [True, "BCTEST_1"], '1', '', True, True, True,

                    nodal_supports= [
                        [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""],

                        [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""]
                                    ],
                    member_hinges=[
                        ["Start", False, False, False, False, False, False, False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""],
                        ["End", False, False, False, False, False, False, False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""]
                                  ]
                            )

    SteelBoundaryConditions(2, [True, "BCTEST_2"], '', '', True, True, True,

                    nodal_supports= [
                        [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""],

                        [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""],

                        [None, SteelBoundaryConditionsSupportType.SUPPORT_TYPE_FIXED_IN_Y_AND_TORSION, False, True, False, True, False, False, False,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, SteelBoundaryConditionsEccentricityTypeZ.ECCENTRICITY_TYPE_USER_VALUE, 0.0, 0.0, 0.0, ""]
                                    ],
                    member_hinges=[
                        ["Start", False, False, False, False, False, False, False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""],
                        ["Inter.", False, False, False, False, False, False, False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""],
                        ["End", True, False, False, True, False, False, True, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ""]
                                  ]
                            )

    bc_1 = Model.clientModel.service.get_steel_boundary_conditions(1)

    assert bc_1.no == 1
    assert bc_1.nodal_supports[0][0].row['rotation'] == 0

    bc_2 = Model.clientModel.service.get_steel_boundary_conditions(2)

    assert bc_2.member_hinges[0][1].row['node_seq_no'] == "Inter."

    Model.clientModel.service.finish_modification()

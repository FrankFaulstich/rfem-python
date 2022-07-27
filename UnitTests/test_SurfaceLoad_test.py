import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from RFEM.Loads.surfaceLoad import SurfaceLoad
from RFEM.LoadCasesAndCombinations.loadCase import LoadCase
from RFEM.LoadCasesAndCombinations.staticAnalysisSettings import StaticAnalysisSettings
from RFEM.TypesForNodes.nodalSupport import NodalSupport
from RFEM.TypesForSurfaces.surfaceSupport import SurfaceSupport
from RFEM.BasicObjects.surface import Surface
from RFEM.BasicObjects.line import Line
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.thickness import Thickness
from RFEM.BasicObjects.material import Material
from RFEM.initModel import Model
from RFEM.enums import *

if Model.clientModel is None:
    Model()

def test_surface_loads():

    Model.clientModel.service.delete_all()
    Model.clientModel.service.begin_modification()

    # Create Material
    Material(1, 'S235')

    # Create Thickness
    Thickness(1, '1', 1, 0.1)

    # Create Nodes
    Node(1, 0.0, 0.0, 0.0)
    Node(2, 4, 0.0, 0.0)
    Node(3, 0, 4.0, 0.0)
    Node(4, 4, 4.0, 0.0)

    # Create Lines
    Line(1, '1 2')
    Line(2, '2 4')
    Line(3, '4 3')
    Line(4, '3 1')

    # Create Surfaces
    Surface(1, '1 2 3 4', 1)

    # Create Nodal Supports
    NodalSupport(1, '1', NodalSupportType.FIXED)
    NodalSupport(2, '2', NodalSupportType.FIXED)
    NodalSupport(3, '3', NodalSupportType.FIXED)
    NodalSupport(4, '4', NodalSupportType.FIXED)

    # Create Static Analysis Settings
    StaticAnalysisSettings(1, '1. Ordnung', StaticAnalysisType.GEOMETRICALLY_LINEAR)

    # Create Load Case
    LoadCase(1, 'Eigengewicht')

    ## Default Surface Load ##
    SurfaceLoad(1, 1, '1', 5000)

    ## Force Type Surface Load with UNIFORM Load Distribution ##
    SurfaceLoad.Force(2, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[5000])

    ## Force Type Surface Load with LINEAR Load Distribution ##
    SurfaceLoad.Force(3, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[5000, 6000, 7000, 2, 3, 4])

    ## Force Type Surface Load with LINEAR_X or LINEAR_Y or LINEAR_Z Load Distribution ##
    SurfaceLoad.Force(4, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[5000, 6000, 3, 4])

    ## Force Type Surface Load with RADIAL Load Distribution ##
    SurfaceLoad.Force(5, 1, '1', SurfaceLoadDirection.LOAD_DIRECTION_GLOBAL_Z_OR_USER_DEFINED_W_TRUE, SurfaceLoadDistribution.LOAD_DISTRIBUTION_RADIAL,
    (5000, 6000, 3, 4, SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS, [1,2,3], [4,5,6]))

    ## Temperature Type Surface Load with UNIFORM Load Distribution ##
    SurfaceLoad.Temperature(6, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[18, 2])

    ## Temperature Type Surface Load with LINEAR Load Distribution ##
    SurfaceLoad.Temperature(7, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[18, 2, 20, 4, 22, 6, 2, 3, 4])

    ## Temperature Type Surface Load with LINEAR_X or LINEAR_Y or LINEAR_Z Load Distribution ##
    SurfaceLoad.Temperature(8, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[18, 2, 20, 4, 2, 3])

    ## Axial Strain Type Surface Load with UNIFORM Load Distribution ##
    SurfaceLoad.AxialStrain(9, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_UNIFORM, load_parameter=[0.5, 1])

    ## Axial Strain Type Surface Load with LINEAR Load Distribution ##
    SurfaceLoad.AxialStrain(10, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR, load_parameter=[0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 2, 3, 4])

    ## Axial Strain Type Surface Load with LINEAR_IN_X Load Distribution ##
    SurfaceLoad.AxialStrain(11, 1, '1', SurfaceLoadDistribution.LOAD_DISTRIBUTION_LINEAR_IN_X, load_parameter=[0.005, 0.006, 0.007, 0.008, 2, 3])

    ## Precamber Type Surface Load ##
    SurfaceLoad.Precamber(12, 1, '1', 50)

    ## Rotary Motion Surface Load ##
    SurfaceLoad.RotaryMotion(13, 1, '1', load_parameter=[1, 2, SurfaceLoadAxisDefinitionType.AXIS_DEFINITION_TWO_POINTS, [1,2,3], [4,5,6]])

    ## Mass Type Surface Load ##
    SurfaceLoad.Mass(14, 1, '1', individual_mass_components=True, mass_parameter=[500, 600, 700])

    SurfaceSupport(1,'1')

    #Calculate_all() # Don't use in unit tests. See template for more info.

    Model.clientModel.service.finish_modification()

from RFEM.initModel import *
from RFEM.enums import *

class OpeningLoad():

    def __init__(self,
                 no: int = 1,
                 load_case_no: int = 1,
                 openings: str = '1',
                 load_distribution = OpeningLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TRAPEZOIDAL,
                 load_direction = OpeningLoadDirection.LOAD_DIRECTION_LOCAL_Z,
                 load_parameter = [],
                 comment: str = '',
                 params: dict = {}):
        '''
        Args:
            load_parameter (list):
                for OpeningLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TRAPEZOIDAL:
                    load_parameter = [magnitude]
                for OpeningLoadDistribution.LOAD_DISTRIBUTION_LINEAR_TRAPEZOIDAL:
                    load_parameter = [magnitude_1, magnitude_2, magnitude_3, node_1, node_2, node_3]
        '''

        # Client model | Opening Load
        clientObject = Model.clientModel.factory.create('ns0:opening_load')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Opening Load No.
        clientObject.no = no

        # Load Case No.
        clientObject.load_case = load_case_no

        # Opening No. (e.g. '5 6 7 12')
        clientObject.openings = ConvertToDlString(openings)

        # Load Distribution
        clientObject.load_distribution = load_distribution.name

        # Load Direction
        clientObject.load_direction = load_direction.name

        # Load Magnitude
        if load_distribution == OpeningLoadDistribution.LOAD_DISTRIBUTION_UNIFORM_TRAPEZOIDAL:
            if load_parameter[0]:
                clientObject.magnitude = load_parameter[0]
        elif load_distribution == OpeningLoadDistribution.LOAD_DISTRIBUTION_LINEAR_TRAPEZOIDAL:
            if load_parameter[0]:
                clientObject.magnitude_1 = load_parameter[0]
            if load_parameter[1]:
                clientObject.magnitude_2 = load_parameter[1]
            if load_parameter[2]:
                clientObject.magnitude_3 = load_parameter[2]

            if load_parameter[3]:
                clientObject.node_1 = load_parameter[3]
            if load_parameter[4]:
                clientObject.node_2 = load_parameter[4]
            if load_parameter[5]:
                clientObject.node_3 = load_parameter[5]

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        for key in params:
            clientObject[key] = params[key]

        # Add Opening Load to client model
        Model.clientModel.service.set_opening_load(load_case_no, clientObject)

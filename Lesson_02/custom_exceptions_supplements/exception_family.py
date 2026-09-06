

class RetroEncabulatorError(Exception):
    """Retro Encabulator failure"""


class UnilateralPhaseDetractorError(RetroEncabulatorError):
    """Failure to unilaterally detract the phase"""


class CardinalGrammeterSyncError(RetroEncabulatorError):
    """Failure to synchronise the cardinal gram meters"""


class ModialInteractionError(RetroEncabulatorError):
    """Modial interaction failed"""


class MagnetoReluctanceError(ModialInteractionError):
    """Magneto not reluctant"""


class CapacitiveDirectance(ModialInteractionError):
    """Capacitive indirectance occured"""

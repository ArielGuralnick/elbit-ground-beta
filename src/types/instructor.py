from src.types.Simulator import Simulator
class Simulator_type:
    MARS = "mars"
    SKY_LARK = "sky_Lark"

class Instructor:
    def __init__(self,name: str, fname: str, simulator: Simulator, simulator_type: Simulator_type = None) -> None:
        if simulator_type is None:
            self.simulator_type = Simulator_type.MARS
        else:
            self.simulator_type = simulator_type

        self.simulator = simulator


def arik_tambal():
    sim = Simulator("sky_Lark", "סקי לארק")
    nir = Instructor("nir", "shtein", sim,  Simulator_type.SKY_LARK)
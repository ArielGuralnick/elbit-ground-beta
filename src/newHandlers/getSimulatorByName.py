from src.newHandlers.simulator import Simulator

def getSimulatorByName(name: str) -> Simulator:
    if name == "mars" :
        return Simulator("mars","מארס", {"computer": "<div><div/>"})
    elif name == "skylaker":
        pass
from typing import Dict

class Simulator:
    englishName: str
    hebrewName: str
    customHTML: Dict[str,str]
    canEdit: bool

    def __init__(self, englishName: str, hebrewName: str, customHTML: Dict[str,str], casEdit: bool):
        self.englishName = englishName
        self.hebrewName = hebrewName
        self.customHTML = customHTML
        self.canEdit = casEdit
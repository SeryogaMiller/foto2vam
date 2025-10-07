# Class to handle configurations

import json
import os
from Utils.Face.vam import VamFace
from Utils.Training.param_generator import ParamGenerator

class Config:
    CONFIG_VERSION = 1

    def __init__(self, configJson, basePath = "" ):
        minJson = os.path.join(basePath, configJson["minJson"]) if "minJson" in configJson else None
        maxJson = os.path.join(basePath, configJson["maxJson"]) if "maxJson" in configJson else None
        self._baseFace = VamFace( os.path.join(basePath, configJson["baseJson"]), minJson, maxJson )
        self._baseFace.trimToAnimatable()

        self._paramShape = None
        angles = set()
        self._input_params = self._parseParams(configJson.get("inputs", []), angles)
        self._output_params = self._parseParams(configJson.get("outputs", []), angles)

        self._angles = sorted(list(angles))

    def _parseParams(self, params, angles):
        """Parse parameters and collect angles."""
        parsed_params = []
        for param in params:
            try:
                paramName = param["name"]
                paramList = []
                for paramParam in param["params"]:
                    paramList.append({"name": paramParam["name"], "value": paramParam["value"]})
                    if paramParam["name"] == "angle":
                        angles.add(float(paramParam["value"]))
                parsed_params.append({"name": paramName, "params": paramList})
            except Exception as e:
                print(f"Error parsing parameter: {e}")
        return parsed_params

    @staticmethod
    def createFromFile( fileName ):
        with open(fileName, 'r') as f:
            jsonData = json.load(f)

        if "config_version" in jsonData and jsonData["config_version"] != Config.CONFIG_VERSION:
            raise Exception("Config version mismatch! File was {}, reader was {}".format(jsonData["config_version"], Config.CONFIG_VERSION ) )

        return Config( jsonData, os.path.dirname(fileName) )

    def getBaseFace(self):
        return self._baseFace

    def getShape(self):
        return self._paramShape

    def getAngles(self):
        return self._angles

    def generateParams(self, relatedFiles ):
        if self._paramShape is None:
            paramGen = ParamGenerator( self._input_params, self._angles, relatedFiles, self._baseFace )
            inputParams = paramGen.getParams()
            inputLen = len(inputParams)
            paramGen = ParamGenerator( self._output_params, self._angles, relatedFiles, self._baseFace )
            outputParams = paramGen.getParams()
            outputLen = len(outputParams)
            self._paramShape = (inputLen, outputLen)
            outParams = inputParams + outputParams
        else:
            paramGen = ParamGenerator( self._input_params + self._output_params, self._angles, relatedFiles, self._baseFace )
            outParams = paramGen.getParams()
        return outParams

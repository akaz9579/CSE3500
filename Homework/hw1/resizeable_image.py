import os
import numpy as np
import imagematrix
from PIL import Image


class ResizeableImage(imagematrix.ImageMatrix):
    def __init__(self, image):
        #path fix for test cause idk why it no workie 
        if isinstance(image, str) and not os.path.isabs(image):
            base_dir = os.path.dirname(os.path.abspath(__file__))
            image = os.path.join(base_dir, image)
        super().__init__(image)

    def best_seam(self, dp=True):
       
        width, height = self.width, self.height
        energy = [[self.energy(x, y) for x in range(width)] for y in range(height)]

        if dp:
            dpTable = [[0] * width for _ in range(height)]
            parent = [[None] * width for _ in range(height)]
            for x in range(width):
                dpTable[0][x] = energy[0][x]
                parent[0][x] = None
            for y in range(1, height):
                for x in range(width):
                    minEnergy = dpTable[y-1][x]
                    minParent = x
                    if x > 0 and dpTable[y-1][x-1] < minEnergy:
                        minEnergy = dpTable[y-1][x-1]
                        minParent = x-1
                    if x < width-1 and dpTable[y-1][x+1] < minEnergy:
                        minEnergy = dpTable[y-1][x+1]
                        minParent = x+1
                    dpTable[y][x] = energy[y][x] + minEnergy
                    parent[y][x] = minParent
            
            minEndX = 0
            minVal = dpTable[height-1][0]
            for x in range(width):
                if dpTable[height-1][x] < minVal:
                    minVal = dpTable[height-1][x]
                    minEndX = x
            seam = []
            x = minEndX
            for y in reversed(range(height)):
                seam.append((x, y))
                x = parent[y][x] if parent[y][x] is not None else x
            seam.reverse()
            return seam
        else:
            def findSeam(y, x):
                if y == height-1:
                    return energy[y][x], [(x, y)]
                nextSteps = []
                for dx in [-1, 0, 1]:
                    nx = x + dx
                    if 0 <= nx < width:
                        stepEnergy, path = findSeam(y+1, nx)
                        nextSteps.append((stepEnergy, path, nx))
                minStep = min(nextSteps, key=lambda t: t[0])
                totalEnergy = energy[y][x] + minStep[0]
                path = [(x, y)] + minStep[1]
                return totalEnergy, path
            bestTotal = None
            bestPath = None
            for x in range(width):
                total, path = findSeam(0, x)
                if bestTotal is None or total < bestTotal:
                    bestTotal = total
                    bestPath = path
            return bestPath


"""

NOo dp:: naive

    def bestSeamNonDP(self):
        lowestEnergy = np.inf
        bestSeam = None
        for startC in range(self.width):
            nodeList = [{"C": startC, 
            "R": 0, 
            "totalEnergy": self.energy(startC, 0), 
            "pathSeam": [(startC, 0)]}]

            while nodeList:
                currentNode = nodeList.pop()
                if currentNode["R"] == self.height - 1:
                    if currentNode["totalEnergy"] < lowestEnergy:
                        lowestEnergy = currentNode["totalEnergy"]
                        bestSeam = currentNode["pathSeam"]
                    continue
                for colShift in range(-1, 2):
                    nextC = currentNode["C"] + colShift
                    nextR = currentNode["R"] + 1
                    if nextC < 0 or nextC >= self.width:
                        continue
                    if nextR >= self.height:
                        continue
                    nextEnergy = currentNode["totalEnergy"] + self.energy(nextC, nextR)
                    if nextEnergy > lowestEnergy:
                        continue
                    nodeList.append({
                        "C": nextC,
                        "R": nextR,
                        "totalEnergy": nextEnergy,
                        "pathSeam": currentNode["pathSeam"] + [(nextC, nextR)]
                    })
        return bestSeam












"""


"""
dp:



 width, height = self.width, self.height
        energy = [[self.energy(x, y) for x in range(width)] for y in range(height)]

        if dp:
            dpTable = [[0] * width for _ in range(height)]
            parent = [[None] * width for _ in range(height)]
            for x in range(width):
                dpTable[0][x] = energy[0][x]
                parent[0][x] = None
            for y in range(1, height):
                for x in range(width):
                    minEnergy = dpTable[y-1][x]
                    minParent = x
                    if x > 0 and dpTable[y-1][x-1] < minEnergy:
                        minEnergy = dpTable[y-1][x-1]
                        minParent = x-1
                    if x < width-1 and dpTable[y-1][x+1] < minEnergy:
                        minEnergy = dpTable[y-1][x+1]
                        minParent = x+1
                    dpTable[y][x] = energy[y][x] + minEnergy
                    parent[y][x] = minParent
            
            minEndX = 0
            minVal = dpTable[height-1][0]
            for x in range(width):
                if dpTable[height-1][x] < minVal:
                    minVal = dpTable[height-1][x]
                    minEndX = x
            seam = []
            x = minEndX
            for y in reversed(range(height)):
                seam.append((x, y))
                x = parent[y][x] if parent[y][x] is not None else x
            seam.reverse()
            return seam
        else:
            def findSeam(y, x):
                if y == height-1:
                    return energy[y][x], [(x, y)]
                nextSteps = []
                for dx in [-1, 0, 1]:
                    nx = x + dx
                    if 0 <= nx < width:
                        stepEnergy, path = findSeam(y+1, nx)
                        nextSteps.append((stepEnergy, path, nx))
                minStep = min(nextSteps, key=lambda t: t[0])
                totalEnergy = energy[y][x] + minStep[0]
                path = [(x, y)] + minStep[1]
                return totalEnergy, path
            bestTotal = None
            bestPath = None
            for x in range(width):
                total, path = findSeam(0, x)
                if bestTotal is None or total < bestTotal:
                    bestTotal = total
                    bestPath = path
            return bestPath








"""
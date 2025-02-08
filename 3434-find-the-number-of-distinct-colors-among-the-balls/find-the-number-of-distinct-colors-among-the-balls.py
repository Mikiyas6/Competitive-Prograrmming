class Solution:
    def queryResults(self, limit, queries):
        distinct = []
        colorMapping = {}
        ballMapping = {}

        for label, color in queries:
            if label in ballMapping:
                oldColor = ballMapping[label]
                colorMapping[oldColor] = colorMapping.get(oldColor, 0) - 1
                if colorMapping[oldColor] == 0:
                    del colorMapping[oldColor]

            colorMapping[color] = colorMapping.get(color, 0) + 1
            ballMapping[label] = color

            distinct.append(len(colorMapping))

        return distinct
def minCost(colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """

        kMax = 0
        i = 0

        while i < len(colors):
            j = i + 1

            while j < len(colors) and colors[j] == colors[i]:
                j += 1

            if j < len(colors) and colors[j] == colors[i] and i > 0:
                i += 1
            else:
                kMax += sum(neededTime[i:j]) - max(neededTime[i:j])
                print(f"i: {i}; j: {j}; kMax: {kMax}; sum(neededTime[i:j]: {sum(neededTime[i:j])}; max(neededTime[i:j]))")

            i = j

        return kMax
    
colors1 = "cddcdcae"
neededTime1 = [4,8,8,4,4,5,4,2]

print(minCost(colors1, neededTime1))

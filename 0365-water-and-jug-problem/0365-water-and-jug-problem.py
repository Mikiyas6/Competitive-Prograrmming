class Solution(object):
   def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        x = self.gcd(jug1Capacity, jug2Capacity)
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        return targetCapacity % x == 0

   def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
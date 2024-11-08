class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        flightrecords = {}
        for flight in flights:
            if flight[0] not in flightrecords:
                flightrecords[flight[0]]={flight[1]:flight[2]}
            else:
                flightrecords[flight[0]][flight[1]]=flight[2]
            
        shortestdist = {}
        minHeap = []
        heapq.heappush(minHeap,(0,(src,0)))

        while minHeap and len(shortestdist)!=n:
    
            weight,node = heapq.heappop(minHeap)
            if node[0] in shortestdist :
                if node[1]<shortestdist[node[0]]:
                    shortestdist[node[0]]=node[1]
                else:
                    continue
            else:
                shortestdist[node[0]] = node[1] 
            
            if node[0]==dst:
                return weight


            if flightrecords.get(node[0]):
                for no,we in flightrecords[node[0]].items():
                    if n not in shortestdist and (node[1]<k or no==dst):
                        heapq.heappush(minHeap,(weight+we,(no,node[1]+1)))

    
        return -1
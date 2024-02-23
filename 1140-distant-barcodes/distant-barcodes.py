class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        # Count the frequency of each barcode
        barcode_count = {}
        for barcode in barcodes:
            barcode_count[barcode] = barcode_count.get(barcode, 0) + 1
        
        # Create a priority queue (max heap) based on barcode frequency
        pq = [(-freq, barcode) for barcode, freq in barcode_count.items()]
        heapq.heapify(pq)
        
        result = []
        while len(pq) >= 2:
            freq1, barcode1 = heapq.heappop(pq)
            freq2, barcode2 = heapq.heappop(pq)
            
            # Add the barcodes to the result array
            result.extend([barcode1, barcode2])
            
            # Decrease the frequencies
            if freq1 < -1:
                heapq.heappush(pq, (freq1 + 1, barcode1))
            if freq2 < -1:
                heapq.heappush(pq, (freq2 + 1, barcode2))
        
        # Add any remaining barcode with non-zero frequency
        if pq:
            freq, barcode = heapq.heappop(pq)
            result.append(barcode)
        
        return result
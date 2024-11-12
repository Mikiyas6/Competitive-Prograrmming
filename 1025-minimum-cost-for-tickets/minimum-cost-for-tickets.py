class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        _1day_pass, _7day_pass, _30day_pass = 0, 1, 2
        
        travel_days = set(days)
        
        last_traverl_day = days[-1]
        
        dp_cost = [  0 for _ in range(last_traverl_day+1)]
    
        for day_i in range(1, last_traverl_day+1):
            
            if day_i not in travel_days:
                
                dp_cost[day_i] = dp_cost[day_i - 1]
            
            else:
                dp_cost[day_i] = min(   dp_cost[ day_i - 1 ]  + costs[ _1day_pass ],
                                        dp_cost[ max(day_i - 7, 0) ]  + costs[ _7day_pass ],
                                        dp_cost[ max(day_i - 30, 0) ] + costs[ _30day_pass ]     )
        
        return dp_cost[last_traverl_day]
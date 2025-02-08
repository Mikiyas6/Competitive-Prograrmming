class Solution:
    def printVertically(self, s: str) -> List[str]:
        my_list=s.split(" ")
        my_final_result=[]
        max_length_item = max(my_list, key=len)
        for index in range(len(max_length_item)):
            for item in my_list:
                if(index<len(item)):
                    my_final_result.append(item[index])
                else:
                    my_final_result.append(" ")
            my_final_result.append(",")
        my_final_result.pop()   
        ###################################
        result = []
        string = []
        for value in "".join(my_final_result):
            if value == ",":
                result.append("".join(string).rstrip(" "))
                string = []
            else:
                string.append(value)
        result.append("".join(string).rstrip(" "))
        return result
        #####################################
        new_list=[item.rstrip(" ") for item in my_final_result]  
        temp="".join(new_list)    
        return temp.split(",")
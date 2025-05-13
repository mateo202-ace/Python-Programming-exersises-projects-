def group_by_first_letter(strings):
   new_list = {}

   for string in strings:  
        new_key = string[0]  
        
       
        if new_key in new_list:
            new_list[new_key].append(string)
        else:
            
            new_list[new_key] = [string]
    
   return new_list


strings = ["apple", "banana", "avocado", "grape", "blueberry", "apricot"]
print(group_by_first_letter(strings))

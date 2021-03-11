#Plan hunt through longest path and to get maximum boars
import sys 

class boarhuntpath:
    #Step1:Algorithm To find path commbinations
    def pathpairs(hunting_map):
        path_pairs = []
        
        for i in range(0,len(hunting_map)):
            for j in range(0,len(list(hunting_map.values())[i])):
                k = (list(hunting_map.keys())[i],list(list(hunting_map.values())[i])[j])
                path_pairs.append(k)
    
        return path_pairs
    
    #Step2: Algorithm To find the all possible paths
    def allpaths(path_pairs):
            
        path_combination = []
        complete_paths = []
    
        path_pairs1 = path_pairs
        
        while path_pairs1 != []:
            for i in range(0,len(path_pairs1)):
                for j in range(0,len(path_pairs)):
                    if path_pairs1[i][len(path_pairs1[1])-1] == path_pairs[j][0]:
                        k = (path_pairs1[i]+path_pairs[j])
                        path_combination.append(k)
                        if k[len(k)-1] == 'choppa':
                            complete_paths.append(list(dict.fromkeys(k)))
            path_pairs1 = path_combination
            path_combination = []
            
        return complete_paths
    
    #Step3: To find longest paths for Duthc, Dylan
    def maxpath(complete_paths):
        
        max_len = 0 
        max_lis = []
    
        for li in complete_paths:
            n = len(li) 
            if n > max_len: # if the current list has a length greater than what we thought was the maximum length...
                max_len = n 
                max_lis = [li] # discard the previous lists (which are shorter), and include the current one
            elif n == max_len and len(max_lis) < 2: # if the current list has the same length as what we think to be the maximum length and only 2 is required
                max_lis.append(li) # add the current list to the set of maximum length lists
    
        return max_lis

# Step4: To calculate the no. of boars hunted and display
class boarhuntcalc:    
    def noofboar(path_of_dutch,path_of_dylan):
        stamina_dutch = 3
        stamina_dylan = 3
        stamina_hunt = 1
        stamina_travel = 1
        stamina_rest = 2
        boar_hunt = 0
        
        
        for n in range(0,len(path_of_dutch)-1): #looping to go to all nodes in the longest path
            if n != 0 : #stamina reduced due to travel
                stamina_dutch = stamina_dutch - stamina_travel
                stamina_dylan = stamina_dylan - stamina_travel 
            no_of_boar = 3
            if path_of_dutch[n] == path_of_dylan[n]:
                if stamina_dutch > 1 and  stamina_dylan > 1 : #hunt till the stamina is grater than 1
                    while stamina_dutch > 1 and  stamina_dylan > 1 and no_of_boar > 0:
                        boar_hunt = boar_hunt + 1
                        stamina_dutch = stamina_dutch - stamina_hunt/2
                        stamina_dylan = stamina_dylan - stamina_hunt/2
                        no_of_boar = no_of_boar - 1
                elif stamina_dutch <= 1 and  stamina_dylan <= 1: #rest (one stamina is always sustained for travel to next node and to take rest)
                   while stamina_dutch <= 1 and  stamina_dylan <= 1:
                       stamina_dutch = stamina_dutch + stamina_rest
                       stamina_dylan = stamina_dylan + stamina_rest
            if path_of_dutch[n] != path_of_dylan[n]:
               if stamina_dutch > 1:  #hunt till the stamina is grater than 1
                    while stamina_dutch > 1 and no_of_boar > 0 :
                        boar_hunt = boar_hunt + 1
                        stamina_dutch = stamina_dutch - stamina_hunt
                        no_of_boar = no_of_boar - 1
               elif stamina_dutch <= 1:  #rest (one stamina is always sustained for travel to next node and to take rest)
                   while stamina_dutch <= 1:
                       stamina_dutch = stamina_dutch + stamina_rest
               if stamina_dylan > 1 :  #hunt till the stamina is grater than 1
                    while stamina_dylan > 1 and no_of_boar > 0:
                        boar_hunt = boar_hunt + 1
                        stamina_dylan = stamina_dylan - stamina_dylan
                        no_of_boar = no_of_boar -1
               elif stamina_dylan <= 1: #rest (one stamina is always sustained for travel to next node and to take rest)
                   while stamina_dylan <= 1:
                       stamina_dylan = stamina_dylan + stamina_rest
        
        
        sys.stdout.write('Path of Dutch: ' + str(path_of_dutch) + '\n')
        sys.stdout.write('Path of Dylan: ' + str(path_of_dylan) + '\n')
        sys.stdout.write('Total no. of boars hunted: ' + str(boar_hunt))
    
class boarhuntmain:
    def main():
        prey = 0
        hunting_map = {
          'A':['B','C','K'],
          'B':['D','E'],
          'C':['E','G','H'],
          'D':['E','F'],
          'E':['G','I','F'],
          'F':['I','J'],
          'G':['I','K'],
          'H':['I','F'],
          'I':['K'],
          'J':['K'],
          'K':['choppa']
        }
     
        #Step1: To find path commbinations
    
        path_pairs = boarhuntpath.pathpairs(hunting_map)
                
        #Step2: Algorithm To find the all possible paths
        
        complete_paths = boarhuntpath.allpaths(path_pairs)
            
        #Step3: To find longest paths for Duthc,Dylan
          
        max_lis = boarhuntpath.maxpath(complete_paths)
    
        path_of_dutch= max_lis[0] # get the maximum length lists for dutch
        path_of_dylan= max_lis[1] # get the maximum length lists for dylan
        
        # Step4: To calculate the no. of boars hunted and display
        boarhuntcalc.noofboar(path_of_dutch,path_of_dylan)

#To display output
boarhuntmain.main()


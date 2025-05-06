nb_layers=int(input("number of layer"))
layer=0
layer_states=[]
while layer<nb_layers:
    state=int(input("particles=1 ; no particles=0"))
    subset=int(input("how many layers ?"))
    for i in range (subset):
        layer_states.append(state)
    layer+=subset
    
#cutting if too many values    
n=layer-nb_layers
layer_states = layer_states[:-n] #if n <= len(my_list) else [] 

    
#saving the result    
file_name=input("filename for print (must be the exact same as the sliced part)")
#layer_states.save(f"/home/alchemy/LAYERS/{file_name}.txt")


        
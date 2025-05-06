import questionary
import os


def resin_selection():
    answer = questionary.select(
    "Select resin:",
    choices=[
        "BA/HEMA 1",
        "BA/HEMA 2",
        "PEGDA/Water",
        "COTS black",
        "Custom set"
    ]
    ).ask()
    if answer=="BA/HEMA 1":
        exp_time=180
        exp_time_first=200 
    elif answer=="BA/HEMA 2":
        exp_time=200
        exp_time_first=220        
    elif answer=="PEGDA/Water":
        exp_time=25
        exp_time_first=96        
    elif answer=="COTS black":
        exp_time=2.8
        exp_time_first=12
    else:
        exp_time=int(input("exposure_time"))
        exp_time_first=int(input("exposure_time first layer"))        
    return exp_time, exp_time_first

# exp_time, exp_time_first=resin_selection()
# print(exp_time, exp_time_first)


def file_def(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    
    answer = questionary.select(
    "Select folder:",
    choices=folders
    ).ask()
    return answer

# a=file_def("C:/Users/arnau/OneDrive/Desktop/PDM - Master thesis/")
# print(a)

import os
import sys
from datetime import datetime

# delay start until sunday...

date = datetime.today().strftime("%Y-%m-%d")

command = "python3 run_forecast.py -d "+date
print("Command: ", command)
os.system(command)

os.chdir("../../covid19-forecast-hub/")

print(os.getcwd())

os.system("git checkout cu-boulder") # my branch is called cu-boulder

os.system("cp ~/Dropbox/nerd_stuff/postdoc/code/covid-forecast-hub/"+\
           "results/"+date+"-CUBoulder-COVIDLSTM.csv ./data-processed/"+\
           "CUBoulder-COVIDLSTM/")

os.system("git add .")

os.system("git commit -m 'cu boulder forecast'")

os.system("git push --set-upstream origin cu-boulder")

os.system("git fetch upstream")

os.system("git checkout origin")

os.system("git merge origin/cu-boulder")

# then do pull request

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

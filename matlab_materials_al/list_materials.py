from pathlib import Path
import shutil
from collections import defaultdict
import json



the_dir = Path()
all_suffixes = ["**/*pdf","**/*pptx","**/*docx","**/*.m", "**/*.tex",
                "**/*.txt", "**/*png"]
keep_dict=dict()
for a_suffix in all_suffixes:
    all_files = list(the_dir.glob(a_suffix))
    the_list = []
    for the_file in all_files:
        the_list.append(str(the_file))
    keep_dict[a_suffix] = the_list

with open("file_index.json",'w') as outfile:
    json.dump(keep_dict,outfile,indent=4)
    

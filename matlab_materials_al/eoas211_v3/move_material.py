from pathlib import Path
import shutil

the_dir = Path()
dest_dir = Path().home() / "repos/eoas_tlef/matlab_code"
all_suffixes = ["**/*.m"]
for a_suffix in all_suffixes:
    all_files = list(the_dir.glob(a_suffix))
    for the_file in all_files:
        rel_path = the_file.relative_to(the_dir)
        new_name = dest_dir / rel_path
        print(new_name)
        print(rel_path)
        new_name.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy(the_file,new_name)

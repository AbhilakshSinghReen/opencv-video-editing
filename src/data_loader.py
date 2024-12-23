from os import listdir
from os.path import dirname as path_dirname, join as path_join


src_dir = path_dirname(__file__)
repo_dir = path_dirname(src_dir)
inputs_dir = path_join(repo_dir, "inputs")
outputs_dir = path_join(repo_dir, "outputs")


def get_input_files():
    input_files = listdir(inputs_dir)
    if ".gitkeep" in input_files:
        input_files.remove(".gitkeep")
    
    input_files = [path_join(inputs_dir, filename) for filename in input_files]
    return input_files

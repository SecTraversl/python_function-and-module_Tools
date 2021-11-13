# %%
#######################################
def get_myfunctions_count():
    import pathlib
    import os
    import subprocess
#
    homepath = pathlib.Path.home()
    fullpath = homepath / 'Temp/pyplay/IMPORT_functions/Python_3.8_Tools/modules'
    # Save path of the original_directory
    orig_dir = os.getcwd()
    # Change directories
    os.chdir(fullpath)
#
    prochandle = subprocess.Popen('grep "^def" *_funcs.py | grep -v "^all_funcs.py" | wc -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output, error = prochandle.communicate()
    results = output.decode().strip()
#
    # Return to original directory
    os.chdir(orig_dir)
    return results


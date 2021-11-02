# %%
#######################################
def get_myfunctions_name():
    import pathlib
    import os
    import subprocess
    
    homepath = pathlib.Path.home()
    fullpath = homepath / 'Temp/pyplay/IMPORT_functions/Python_3.8_Tools/modules'
    os.chdir(fullpath)

    print('\nNow running ... :  cd ~/Temp/pyplay/IMPORT_functions/Python_3.8_Tools/modules')
    print('Now running ... :  grep "^def" *_funcs.py | grep -v "^all_funcs.py"\n\n')
    prochandle = subprocess.Popen('grep "^def" *_funcs.py | grep -v "^all_funcs.py"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output, error = prochandle.communicate()
    results = output.decode().splitlines()
    return results


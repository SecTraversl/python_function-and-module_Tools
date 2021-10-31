# %%
#######################################
def invoke_module_reload_star(module_name: str):
    """For a given module_name reloads the respective module by that name.

    Reference:
        https://stackoverflow.com/questions/7271082/how-to-reload-a-modules-function-in-python\n
        https://realpython.com/lessons/reloading-module/\n
        https://www.tutorialspoint.com/the-implementation-of-import-in-python-importlib\n
        https://stackoverflow.com/questions/10675054/how-to-import-a-module-in-python-with-importlib-import-module\n
        https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path\n
        https://docs.python.org/3/tutorial/modules.html\n

    Args:
        module_name (str): Reference the name of the module you want to reload.
    """
    print(f'\n1. Execute the following:\n\timport {module_name}\n')
    print(f'\n2. Execute the following:\n\tinvoke_module_reload(\'{module_name}\'\n')
    print(f'\n3. Execute the following:\n\tfrom {module_name} import *\n')


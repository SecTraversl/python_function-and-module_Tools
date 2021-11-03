# %%
#######################################
def get_myfunctions_timesorted():
    """Returns the functions I have created along with and sorted by the last modified time of the function .py file.
    
    Example:
        >>> from pprint import pprint\n
        >>> results = get_myfunctions_timesorted()\n
        >>> pprint(results)\n
        [('2021-10-22 07:20:11', 'pandas_funcs/sort_by_multiple_indexes.py'),\n
        ('2021-10-22 07:21:19',
        'pandas_funcs/sort_by_multiple_indexes_granular_reverse.py'),\n
        ('2021-10-22 07:24:13', 'pandas_funcs/get_group_members.py'),\n
        ('2021-10-22 07:27:05', 'system_funcs/get_object_memory_usage.py'),\n
        ('2021-10-22 07:27:45', 'system_funcs/get_object_memory_address.py'),\n
        ('2021-10-22 07:28:49', 'system_funcs/get_current_python_path.py'),\n
        ('2021-10-22 07:29:21', 'system_funcs/get_current_python_version.py'),\n
        ('2021-10-22 07:31:06', 'format_funcs/format_header_break.py'),\n
        ('2021-10-22 07:32:18', 'format_funcs/format_header_text.py')]\n
    """
    import pathlib
    import os
#
    homepath = pathlib.Path.home()
    thepath = homepath / 'Temp/pyplay/IMPORT_functions/Python_3.8_Tools'
    os.chdir(thepath)
#

    def convert_timestamp(timestamp: float, tenthousandths=False):
        from datetime import datetime
        if tenthousandths:
            readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        return readable_time
#
    # Here we isolate the functions in the directories that we want, then return the timestamps as the first part of the tuple and the parent dir/file as the second part
    results_list = [ ( convert_timestamp(f.stat().st_mtime), '/'.join(f.parts[-2:]) ) for f in thepath.rglob('*') if f.name.endswith('.py') and '/modules/' not in f.as_posix() and '/all_funcs/' not in f.as_posix() ]
#
    # We then sort on that formatted timestamp string
    results_list = sorted(results_list, key=lambda x: x[0])
    return results_list


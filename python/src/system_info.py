# filepath: python-project/src/system_info.py

import psutil
import platform

def get_system_info():
    #get system uptime
    uptime = psutil.boot_time()

    try:
        temperature = psutil.sensors_temperatures()
        cpu_temp = temperature['coretemp'][0].current if 'coretemp' in temperature else 'N/A'
    except AttributeError:
        cpu_temp = 'N/A'
    
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Uptime (seconds)": uptime,
        "CPU Temperature (°C)": cpu_temp
    }

    return system_info

if __name__ == "__main__":
    info = get_system_info()
    for key, value in info.items():
<<<<<<< HEAD:python/src/system_info.py
        print(f"{key}: {value}")
=======
        print(f"{key}: {value}")
>>>>>>> 282cef39e5f09756830b0fb72fbe8245abb6929f:src/system_info.py

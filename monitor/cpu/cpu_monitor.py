import psutil

def get_cpu_info():
    #retorna o % de uso da CPU por núcleo
    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
    #retorna o % total de uso da CPU
    cpu_usage_total = round(sum(cpu_usage_per_core) / len(cpu_usage_per_core), 1) if cpu_usage_per_core else 0.0
    #retorna o número de núcleos lógicos
    cpu_logical_core = psutil.cpu_count(logical=True)
    #retorna o número de núcleos físicos
    cpu_physical_core = psutil.cpu_count(logical=False)
    # #retorna o status do CPU
    # cpu_status = psutil.cpu_stats()

    # Frequencia do CPU em Mhz (fixo em Windows)
    try:
        cpu_freq = psutil.cpu_freq()
        if cpu_freq and cpu_freq.current > 0.0:
            cpu_freq_current = cpu_freq.current
            cpu_freq_min = cpu_freq.min
            cpu_freq_max = cpu_freq.max
        else:
            raise ValueError
    except (AttributeError, ValueError, TypeError):
        cpu_freq_current = None
        cpu_freq_min = None
        cpu_freq_max = None
    return {
        "uso_total_percentual" : cpu_usage_total,
        "uso_por_nucleo_percentual" : cpu_usage_per_core,
        "nucleos_logicos" : cpu_logical_core,
        "nucleos_fisicos" : cpu_physical_core,
        # "status_cpu" : {
        #     "ctx_switches" : cpu_status.ctx_switches,
        #     "interrupts" : cpu_status.interrupts,
        #     "soft_interrupts" : cpu_status.soft_interrupts,
        #     "syscalls" : cpu_status.syscalls
        # },
        "frequencia_cpu_mhz" : {
            "current" : cpu_freq_current,
            "min" : cpu_freq_min,
            "max" : cpu_freq_max,
        }
    }



# # CPU ---------------------------------------------------------------------------------
# # CPU percent
# cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
# print("CPU Percent: ",cpu_percent)

# # Deixar True para retornar todos os núcleos, False para retornar apenas a média
# cpu_times_per = psutil.cpu_times_percent(interval=1, percpu=False)
# print("CPU Times Percent: ",cpu_times_per)

# # Caso False retorna apenas o número de núcleos físicos
# # Caso True retorna o número de núcleos lógicos
# num_cpu = psutil.cpu_count(logical=False)
# print("Núcleos: ",num_cpu)

# # Numero de CPU's que podem ser utilizados pelo sistema operacional
# true_cpu = len(psutil.Process().cpu_affinity())
# print("Núcleos Utilizáveis: ",true_cpu)

# # Status do CPU
# cpu_status = psutil.cpu_stats()
# print("CPU Status: ",cpu_status)

# # Frequencia do CPU em Mhz (fixo em Windows)
# cpu_freq = psutil.cpu_freq()
# print("CPU Frequency: ",cpu_freq)

# # Média de system load
# cpu_load = psutil.getloadavg()
# print("CPU Load: ",cpu_load)
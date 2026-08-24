import psutil

# CPU ---------------------------------------------------------------------------------
# CPU percent
cpu_percent = psutil.cpu_percent(interval=1, percpu=False)
print("CPU Percent: ",cpu_percent)

# Deixar True para retornar todos os núcleos, False para retornar apenas a média
cpu_times_per = psutil.cpu_times_percent(interval=1, percpu=False)
print("CPU Times Percent: ",cpu_times_per)

# Caso False retorna apenas o número de núcleos físicos
# Caso True retorna o número de núcleos lógicos
num_cpu = psutil.cpu_count(logical=False)
print("Núcleos: ",num_cpu)

# Numero de CPU's que podem ser utilizados pelo sistema operacional
true_cpu = len(psutil.Process().cpu_affinity())
print("Núcleos Utilizáveis: ",true_cpu)

# Status do CPU
cpu_status = psutil.cpu_stats()
print("CPU Status: ",cpu_status)

# Frequencia do CPU em Mhz (fixo em Windows)
cpu_freq = psutil.cpu_freq()
print("CPU Frequency: ",cpu_freq)

# Média de system load
cpu_load = psutil.getloadavg()
print("CPU Load: ",cpu_load)

# MEMORIA ---------------------------------------------------------------------------------
# Retorna a quantidade de memória virtual disponível, usada, livre, etc.
memoria = psutil.virtual_memory()
print("Memoria: ",memoria)

# DISK ---------------------------------------------------------------------------------
# Caso Falso tenta distinguir entre discos físicos e lógicos e tenta retornar apenas os Fisicos
# Caso True retorna todos os discos

disco = psutil.disk_partitions(all=True)
print("Disco: ",disco)

# Retorna o uso do Disco
disco_uso = psutil.disk_usage('/')
print("Disco Uso: ",disco_uso)

# Retorna o IO do Disco
# Quando perdisk é True, retorna a mesma informação para cada disco fisico
# Caso nowrap for True, retorna o valor acumulado desde a inicialização do sistema
disco_io = psutil.disk_io_counters(perdisk=True, nowrap=True)
print("Disco IO: ",disco_io)

# NETWORK ---------------------------------------------------------------------------------
# Retorna as statisticas de I/O da rede
# Caso pernic for True retorna todas as redes instaladas
# Caso False retorna apenas a ativa
rede = psutil.net_io_counters(pernic=False, nowrap=True)
print("Rede: ",rede)

# Retorna os tipos de IP usado
# inet - IPv4 e IPv6
# inet4 - IPv4
# inet6 - IPv6
# tcp - TCP
# tcp4 - prioriza TCP ao invez de IPv4
# tcp6 - prioriza TCP ao invez de IPv6
# udp - UDP
# udp4 - prioriza UDP ao invez de IPv4
# udp6 - prioriza UDP ao invez de IPv6
# unix - Unix sockets
# all - todos os tipos de IP
# rede_ip = psutil.net_connections(kind='inet4')
# print("Rede IP: ",rede_ip)

# Retorna o endereço associado a cada NIC
# rede_endereco = psutil.net_if_addrs()
# print("Rede Endereço: ",rede_endereco)

# Retorna as estatisticas de cada NIC
rede_estatisticas = psutil.net_if_stats()
print("Rede Estatisticas: ",rede_estatisticas)

# SENSORES ---------------------------------------------------------------------------------
# Retorna o status da bateria do sensor
sensor = psutil.sensors_battery()
print("Sensor: ",sensor)

# BOOT TIME ---------------------------------------------------------------------------------
# Retorna o tempo de boot do sistema
boot_time = psutil.boot_time()
print("Boot Time: ",boot_time)

# USERS ---------------------------------------------------------------------------------
# Retorna os usuários logados no sistema
usuarios = psutil.users()
print("Usuários: ",usuarios)

# PROCESSOS ---------------------------------------------------------------------------------
# Retorna os processos ativos no sistema
# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc.info)

# Retorna quais PIDs existem no sistema
# pids = psutil.pid_exists(7464) # troque o PID para o que deseja verificar
# print("PID x existe: ",pids)

# Retorna qual processo pode ser terminado
procs = psutil.Process().children()
gone, alive = psutil.wait_procs(procs, timeout=3)
print(gone)
print(alive)
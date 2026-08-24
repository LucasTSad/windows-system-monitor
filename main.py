from monitor.cpu.cpu_monitor import get_cpu_info
from monitor.memory.memory_monitor import get_memory_info

cpu_info = get_cpu_info()
mem_info = get_memory_info()

print(f"CPU: {cpu_info}\nMEMORIA: {mem_info}\n")

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
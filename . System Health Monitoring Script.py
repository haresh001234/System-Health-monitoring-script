import psutil
import logging
import datetime

# Configuration
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 90.0
LOG_FILE = "/path/to/system_health.log"

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        alert(f"High disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    processes = [(p.pid, p.info['name']) for p in psutil.process_iter(['name'])]
    return processes

def alert(message):
    logging.warning(message)
    print(message)  # Optional: print to console for immediate feedback

def log_system_health(cpu, memory, disk, processes):
    logging.info(f"CPU Usage: {cpu}%")
    logging.info(f"Memory Usage: {memory}%")
    logging.info(f"Disk Usage: {disk}%")
    logging.info(f"Running Processes: {len(processes)}")

def main():
    logging.info("Starting system health check...")
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_usage()
    processes = check_running_processes()
    log_system_health(cpu, memory, disk, processes)
    logging.info("System health check completed.")

if __name__ == "__main__":
    main()
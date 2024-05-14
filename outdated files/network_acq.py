import csv
import psutil
import subprocess
import time
from speedtest import Speedtest

path = '/home/ldm/Documents/acquired_data'
filename = input("Choose a name for the Network experiment: ")
# Open the CSV file for writing
csv_file = open(f'{path}/{filename}_network_monitor.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Write the header row
csv_writer.writerow(['ElapsedSeconds', 'CPU Usage', 'Memory Usage (MB)', 'Network Received (MB)',
                    'Network Sent (MB)', 'Network Receive Traffic (Mbps)', 'Network Send Traffic (Mbps)',
                    'Latency (ms)', 'Throughput (Mbps)', 'Jitter (ms)', 'Bandwidth (Mbps)'])

# Monitor system usage continuously
try:
    # Get the initial timestamp
    initial_timestamp = time.time()

    # Initialize previous network receive and send values
    network_receive_prev = 0
    network_send_prev = 0

    # Initialize Speedtest object
    speedtest = Speedtest()

    while True:
        # Get the current timestamp
        current_timestamp = time.time()

        # Calculate elapsed seconds
        elapsed_seconds = current_timestamp - initial_timestamp
        print(f'Elapsed time: {elapsed_seconds}')

        # Get CPU usage as a percentage
        cpu_usage = psutil.cpu_percent(interval=None)

        # Get memory usage in megabytes
        memory_usage = psutil.virtual_memory().used / (1024 * 1024)

        # Get network usage in megabytes
        net_io = psutil.net_io_counters()
        network_receive = net_io.bytes_recv / (1024 * 1024)
        network_send = net_io.bytes_sent / (1024 * 1024)

        # Calculate network receive traffic in Mbps
        network_receive_traffic = (net_io.bytes_recv - network_receive_prev) * 8 / elapsed_seconds / (1024 ** 2)

        # Calculate network send traffic in Mbps
        network_send_traffic = (net_io.bytes_sent - network_send_prev) * 8 / elapsed_seconds / (1024 ** 2)

        # Perform a ping to measure latency
        ping_process = subprocess.Popen(['ping', '-c', '1', 'example.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_output, _ = ping_process.communicate()
        ping_output = ping_output.decode()
        ping_time = float(ping_output.split('time=')[1].split()[0])

        # Perform a speed test to measure throughput, jitter, and bandwidth
        speedtest.download()
        speedtest_results = speedtest.results.dict()
        throughput = speedtest_results['download'] / (1024 * 1024)
        jitter = speedtest_results['ping'] - ping_time
        bandwidth = speedtest_results['upload'] / (1024 * 1024)

        # Write the data row to the CSV file
        csv_writer.writerow([elapsed_seconds, cpu_usage, memory_usage, network_receive, network_send,
                             network_receive_traffic, network_send_traffic, ping_time, throughput, jitter, bandwidth])

        # Update the previous network receive and send values
        network_receive_prev = net_io.bytes_recv
        network_send_prev = net_io.bytes_sent

        # Flush the buffer to ensure data is written immediately
        csv_file.flush()

        # Sleep for 0.1 second before collecting the next sample
        time.sleep(0.1)

except KeyboardInterrupt:
    print('\n', 'Stopping acquistion...', '\n', f'Saved path: {path}')
    # User interrupted the program, close the CSV file
    csv_file.close()

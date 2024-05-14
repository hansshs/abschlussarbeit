import csv
import psutil
import time

# Open the CSV file for writing
path = '/home/ldm/Documents/acquired_data/IterAvg'
filename = input("Choose a name for the PID experiment: ")
csv_file = open(f'{path}/{filename}system_monitor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Write the header row
csv_writer.writerow(['ElapsedSeconds', 'CPU Usage (%)', 'Memory Usage (MB)', 'Network Received (MB)', 'Network Sent (MB)', 'Network Receive Traffic (Mbps)', 'Network Send Traffic (Mbps)'])

# Monitor system usage continuously
try:
    # Get the initial timestamp
    initial_timestamp = time.time()

    # Initialize previous network receive and send values
    network_receive_prev = 0
    network_send_prev = 0

    while True:
        # Get the current timestamp
        current_timestamp = time.time()

        # Calculate elapsed seconds
        elapsed_seconds = current_timestamp - initial_timestamp
        #print(f'Elapsed time: {elapsed_seconds}')

        # Get CPU usage as a percentage
        cpu_usage = psutil.cpu_percent(interval=None)

        # Get memory usage in megabytes
        memory_usage = psutil.virtual_memory().used / (1024 * 1024)

        # Get network usage in megabytes
        net_io = psutil.net_io_counters()
        network_receive = net_io.bytes_recv / (1024 * 1024)
        network_send = net_io.bytes_sent / (1024 * 1024)

        # Calculate network receive traffic in Mbps
        network_receive_traffic = (net_io.bytes_recv - network_receive_prev) * 8 / elapsed_seconds / (1024**2)

        # Calculate network send traffic in Mbps
        network_send_traffic = (net_io.bytes_sent - network_send_prev) * 8 / elapsed_seconds / (1024**2)

        # Write the data row to the CSV file
        csv_writer.writerow([elapsed_seconds, cpu_usage, memory_usage, network_receive, network_send, network_receive_traffic, network_send_traffic])

        # Update the previous network receive and send values
        network_receive_prev = net_io.bytes_recv
        network_send_prev = net_io.bytes_sent

        # Flush the buffer to ensure data is written immediately
        csv_file.flush()

        # Sleep for 0.1 second before collecting the next sample
        time.sleep(0.1)

except KeyboardInterrupt:
    # User interrupted the program, close the CSV file
    csv_file.close()


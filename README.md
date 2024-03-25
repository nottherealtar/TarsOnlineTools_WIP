# Network Toolkit

This Python script provides a console-based network toolkit with various functionalities. It's designed to be user-friendly with a menu-driven interface.

## Features

1. **IP Tools**: Network monitoring, device identification, and printing the IP range of the network interface that is currently up.
2. **LAN Tools**: Network scanning to identify devices connected to the network.
3. **Speedtest**: Performs a speedtest and prints the download and upload speed.
4. **Speedtest Advanced**: Performs a speedtest and prints detailed results including ping, server name, and server country.
5. **Device Information**: Prints information about the device running the script, such as OS, hostname, IP address, and MAC address.

## Dependencies

The script uses several libraries including:

- `scapy` for network operations
- `speedtest` for speed testing
- `colorama` and `rich` for console output formatting
- `requests` for HTTP requests
- `netifaces` for network interface information
- `ipaddress` for IP network calculations
- `logging` for logging errors

## Usage

To run the script, use the following command:

```bash
python console.py
```

## Error Handling

The script handles exceptions and logs them for troubleshooting. The log file is named `app.log`.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

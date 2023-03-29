import ping3

hostname = "0.0.0.0"
response_time = ping3.ping(hostname)

if response_time is not None:
    print(f"The Server {hostname} responded in {response_time} seconds")
else:
    print(f"Could not ping the server {hostname}")


# Import    pip install ping3

# Documentation     https://pypi.org/project/ping3/
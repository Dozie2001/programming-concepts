#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""


if __name__ == '__main__':
    import urllib.request
    import sys
    # Check if URL is provided
    if len(sys.argv) < 2:
        print("Error: Please provide a URL.")
        sys.exit(1)
    
    # Get the URL from command-line argument
    url = sys.argv[1]
    # Send a request to the URL
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of X-Request-Id from the header
        x_request_id = response.getheader("X-Request-Id")
        
        if x_request_id is not None:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in the response header.")

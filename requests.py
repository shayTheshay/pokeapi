import requests

def handle_response(url):
    """Handle different HTTP status codes with basic error handling."""
    try:
        response = requests.get(url)

        ## Check status code category
        if 200 <= response.status_code < 300:
            print(f"Success! Status code: {response.status_code}")
            return response
        elif 300 <= response.status_code < 400:
            print(f"Redirection! Status code: {response.status_code}")
            ## For redirection, you might want to follow the redirect
            return response
        elif 400 <= response.status_code < 500:
            print(f"Client error! Status code: {response.status_code}")
            ## Handle client errors
            return response
        elif 500 <= response.status_code < 600:
            print(f"Server error! Status code: {response.status_code}")
            ## Handle server errors
            return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

## Test with different status codes
print("Testing 200 OK:")
handle_response("https://httpbin.org/status/200")

print("\nTesting 404 Not Found:")
handle_response("https://httpbin.org/status/404")

print("\nTesting 500 Internal Server Error:")
handle_response("https://httpbin.org/status/500")


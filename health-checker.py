import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        
        # Check if the response status code indicates that the application is up
        if response.status_code == 200:
            print(f"Application is UP! Status Code: {response.status_code}")
        else:
            print(f"Application is DOWN! Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN! Error: {e}")

if __name__ == "__main__":
    # Replace with your application's URL
    application_url = "http://your-application-url.com/health"
    check_application_health(application_url)

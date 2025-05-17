# test_scalability.py
import requests
from concurrent.futures import ThreadPoolExecutor
import time

API_URL = "http://127.0.0.1:8000/predict"
IMAGE_PATH = "test_images/banana.jpg"
CONCURRENT_USERS = 20
TOTAL_REQUESTS = 100

def send_request():
    try:
        with open(IMAGE_PATH, 'rb') as f:
            start = time.time()
            response = requests.post(API_URL, files={'file': f})
            elapsed = time.time() - start
            
            return {
                'status': response.status_code,
                'time': elapsed,
                'success': response.status_code == 200
            }
    except Exception as e:
        return {'status': str(e), 'time': 0, 'success': False}

def run_test():
    with ThreadPoolExecutor(max_workers=CONCURRENT_USERS) as executor:
        futures = [executor.submit(send_request) for _ in range(TOTAL_REQUESTS)]
        results = [f.result() for f in futures]
        
        # Calculate metrics
        successes = sum(1 for r in results if r['success'])
        avg_time = sum(r['time'] for r in results) / len(results)
        
        print(f"\nResults:")
        print(f"Successful requests: {successes}/{TOTAL_REQUESTS}")
        print(f"Error rate: {(1 - successes/TOTAL_REQUESTS)*100:.1f}%")
        print(f"Average response time: {avg_time:.3f}s")
        print(f"Requests per second: {TOTAL_REQUESTS/sum(r['time'] for r in results):.1f}")

if __name__ == "__main__":
    print(f"Starting test with {CONCURRENT_USERS} concurrent users...")
    run_test()

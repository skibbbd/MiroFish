#!/usr/bin/env python3
"""
Simple API test script for MiroFish in TEST_MODE
Tests all the main endpoints to verify mock data generation is working
"""

import requests
import json
import sys
from typing import Dict, Any

BASE_URL = "http://localhost:5001"
API_PREFIX = "/api/simulation"

class APITester:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.passed = 0
        self.failed = 0
    
    def test_endpoint(self, method: str, endpoint: str, description: str, **kwargs) -> bool:
        """Test an API endpoint and print results"""
        url = f"{self.base_url}{API_PREFIX}{endpoint}"
        try:
            print(f"\n{'='*60}")
            print(f"Test: {description}")
            print(f"Method: {method}")
            print(f"URL: {url}")
            
            if method.upper() == "GET":
                response = requests.get(url, **kwargs)
            elif method.upper() == "POST":
                response = requests.post(url, **kwargs)
            else:
                print(f"❌ Unknown HTTP method: {method}")
                self.failed += 1
                return False
            
            status = response.status_code
            print(f"Status Code: {status}")
            
            if status in [200, 201]:
                try:
                    data = response.json()
                    if data.get('success'):
                        print(f"✅ SUCCESS")
                        print(f"Response Preview:")
                        if 'data' in data:
                            response_data = data['data']
                            if isinstance(response_data, dict):
                                for key in list(response_data.keys())[:3]:
                                    val = response_data[key]
                                    if isinstance(val, list) and len(val) > 3:
                                        print(f"  - {key}: [{len(val)} items]")
                                    elif isinstance(val, (dict, list)):
                                        print(f"  - {key}: {str(val)[:60]}...")
                                    else:
                                        print(f"  - {key}: {val}")
                        self.passed += 1
                        return True
                    else:
                        print(f"❌ FAILED: API returned success=false")
                        print(f"Error: {data.get('error', 'Unknown error')}")
                        self.failed += 1
                        return False
                except json.JSONDecodeError:
                    print(f"❌ FAILED: Could not parse JSON response")
                    print(f"Response: {response.text[:200]}")
                    self.failed += 1
                    return False
            else:
                print(f"❌ FAILED: HTTP {status}")
                print(f"Response: {response.text[:200]}")
                self.failed += 1
                return False
                
        except requests.exceptions.ConnectionError:
            print(f"❌ FAILED: Could not connect to {self.base_url}")
            print(f"   Make sure the backend is running: python backend/run.py")
            self.failed += 1
            return False
        except Exception as e:
            print(f"❌ FAILED: {str(e)}")
            self.failed += 1
            return False
    
    def run_all_tests(self):
        """Run all API tests"""
        print("\n" + "="*60)
        print("MiroFish API Test Suite (TEST_MODE)")
        print("="*60)
        
        # Test 1: Get graph entities
        self.test_endpoint(
            "GET",
            "/entities/test_graph_123",
            "Get all graph entities (no filters)"
        )
        
        # Test 2: Get graph entities with type filter
        self.test_endpoint(
            "GET",
            "/entities/test_graph_123?entity_types=Student,PublicFigure",
            "Get graph entities with type filtering"
        )
        
        # Test 3: Get entities by type
        self.test_endpoint(
            "GET",
            "/entities/test_graph_123/by-type/Student",
            "Get entities filtered by type (Student)"
        )
        
        # Test 4: Get entities by different type
        self.test_endpoint(
            "GET",
            "/entities/test_graph_123/by-type/Organization",
            "Get entities filtered by type (Organization)"
        )
        
        # Test 5: Get single entity detail
        self.test_endpoint(
            "GET",
            "/entities/test_graph_123/entity_test_001",
            "Get single entity details"
        )
        
        # Test 6: Get entities with edge enrichment
        self.test_endpoint(
            "GET",
            "/entities/test_graph_123?enrich=true",
            "Get graph entities with enriched edge information"
        )
        
        # Summary
        print(f"\n" + "="*60)
        print("Test Summary")
        print("="*60)
        print(f"✅ Passed: {self.passed}")
        print(f"❌ Failed: {self.failed}")
        total = self.passed + self.failed
        if total > 0:
            percentage = (self.passed / total) * 100
            print(f"Success Rate: {percentage:.1f}%")
        print("="*60)
        
        return self.failed == 0

def main():
    """Main test runner"""
    print("\nMiroFish API Testing")
    print("Checking if backend is running at http://localhost:5001...\n")
    
    # Quick connectivity test
    try:
        requests.get(f"{BASE_URL}/api/simulation/entities/test", timeout=2)
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend at http://localhost:5001")
        print("\nPlease start the backend first:")
        print("  cd backend && python run.py")
        print("\nOr run both services together:")
        print("  npm run dev")
        sys.exit(1)
    except Exception:
        pass  # Continue with tests
    
    # Run tests
    tester = APITester()
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

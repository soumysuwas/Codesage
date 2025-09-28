#!/usr/bin/env python3
"""
Test script for CodeSage AI Technical Interviewer
Tests both backend and frontend components
"""

import subprocess
import time
import requests
import sys
from pathlib import Path

def test_backend():
    """Test backend server"""
    print("🧪 Testing backend server...")
    
    try:
        # Test health endpoint
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend health check passed: {data['status']}")
            print(f"   Gemini configured: {data['gemini_configured']}")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend not responding: {e}")
        return False

def test_frontend():
    """Test frontend server"""
    print("🧪 Testing frontend server...")
    
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend server responding")
            return True
        else:
            print(f"❌ Frontend server failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend not responding: {e}")
        return False

def test_api_endpoints():
    """Test API endpoints"""
    print("🧪 Testing API endpoints...")
    
    try:
        # Test create interview
        response = requests.post("http://localhost:8000/api/interviews", 
                               json={"candidate_name": "Test User", "difficulty": "easy"})
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Create interview endpoint working")
            interview_id = data['interview']['id']
            
            # Test get interview
            response = requests.get(f"http://localhost:8000/api/interviews/{interview_id}")
            if response.status_code == 200:
                print("✅ Get interview endpoint working")
                return True
            else:
                print(f"❌ Get interview endpoint failed: {response.status_code}")
                return False
        else:
            print(f"❌ Create interview endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ API test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing CodeSage AI Technical Interviewer System")
    print("=" * 60)
    
    # Test backend
    backend_ok = test_backend()
    
    # Test frontend
    frontend_ok = test_frontend()
    
    # Test API endpoints
    api_ok = test_api_endpoints()
    
    print("\n" + "=" * 60)
    print("📊 Test Results:")
    print(f"Backend: {'✅ PASS' if backend_ok else '❌ FAIL'}")
    print(f"Frontend: {'✅ PASS' if frontend_ok else '❌ FAIL'}")
    print(f"API Endpoints: {'✅ PASS' if api_ok else '❌ FAIL'}")
    
    if backend_ok and frontend_ok and api_ok:
        print("\n🎉 All tests passed! System is ready.")
        print("\n🌐 Access the application at: http://localhost:3000")
        return True
    else:
        print("\n❌ Some tests failed. Please check the logs above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

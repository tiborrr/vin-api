# A sample VIN to test with
TEST_VIN = "5UXWX7C5*BA"

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "VIN Decoder" in response.text

def test_validate_vin_simple(client):
    response = client.get(f"/api/v1/vin/{TEST_VIN}/simple")
    assert response.status_code == 200
    data = response.json()
    assert data["vin"] == TEST_VIN
    assert data["wmi"] == "5UX"
    assert data["model_year"] == 2011
    assert "is_valid" in data

def test_validate_vin_complex(client):
    response = client.get(f"/api/v1/vin/{TEST_VIN}/decode")
    assert response.status_code == 200
    data = response.json()
    assert data["vin"] == TEST_VIN
    assert "details" in data
    # Check if a known field was decoded
    make_detail = next((item for item in data["details"] if item["code"] == "Make"), None)
    assert make_detail is not None
    assert make_detail["value"] == "BMW"

def test_invalid_vin(client):
    response = client.get("/api/v1/vin/INVALIDVIN123/simple")
    # Our DB logic might just return nulls or empty for invalid vins.
    # The simple endpoint raises 404 if no row is returned, but scalar functions usually return a row with nulls.
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is False

def test_validate_vin_bulk_simple(client):
    vins_to_test = [TEST_VIN, "INVALIDVIN123", "1G1RC6E4*BU"]
    response = client.post("/api/v1/vin/bulk-simple", json={"vins": vins_to_test})
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    results = data["results"]
    assert len(results) == 3
    
    # First VIN is valid BMW pattern (but invalid check digit due to wildcard)
    assert results[0]["vin"] == TEST_VIN
    assert results[0]["is_valid"] is False
    assert results[0]["wmi"] == "5UX"
    
    # Second VIN is completely invalid
    assert results[1]["vin"] == "INVALIDVIN123"
    assert results[1]["is_valid"] is False
    
    # Third VIN is a generic format pattern
    assert results[2]["vin"] == "1G1RC6E4*BU"
    assert results[2]["is_valid"] is False

def test_concurrent_requests(client):
    import concurrent.futures

    def make_request():
        return client.get(f"/api/v1/vin/{TEST_VIN}/simple")

    # Send 50 concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(make_request) for _ in range(50)]
        for future in concurrent.futures.as_completed(futures):
            response = future.result()
            assert response.status_code == 200
            data = response.json()
            assert data["is_valid"] is False

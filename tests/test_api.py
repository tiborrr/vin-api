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

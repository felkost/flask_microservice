import json


def test_ping(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.get('/ping')

    data = json.loads(resp.data.decode())

    # Then
    # print('resp --> ', resp.status_code)
    # print('resp.data --> ', resp.data)
    # print('data --> ', data)
    # assert False

    assert resp.status_code == 200
    assert 'pong' in data['message']
    assert 'success' in data['status']

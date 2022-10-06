def main():
  data = []

  for i in range(1, 5):
    data.append({
      'id': i,
      'name': 'John Doe',
      'email': 'hoge@hoge.hoge',
      'password': '00000000-0000-0000-0000-000000000000',
      'bus': {
        'id': i,
        'drive': True,
        'start': '00:00',
        'end': '00:00',
        'createdAt': '2020-01-01 00:00:00',
        'driver': {
          'id': 1,
          'name': 'John Doe',
          'email': 'johndoe@hoge.hoge',
        },
        'passengers': [
          {
            'id': 1,
            'name': 'Bus Passenger 1',
            'status': True,
            'uuid': '00000000-0000-0000-0000-000000000000',
          },
          {
            'id': 2,
            'name': 'Bus Passenger 1',
            'status': True,
            'uuid': '00000000-0000-0000-0000-000000000000',
          },
          {
            'id': 3,
            'name': 'Bus Passenger 1',
            'status': True,
            'uuid': '00000000-0000-0000-0000-000000000000',
          },
          {
            'id': 4,
            'name': 'Bus Passenger 1',
            'status': True,
            'uuid': '00000000-0000-0000-0000-000000000000',
          },
          {
            'id': 5,
            'name': 'Bus Passenger 1',
            'status': True,
            'uuid': '00000000-0000-0000-0000-000000000000',
          },
        ]
      }
    })

  return data

if __name__ == "__main__":
  print(main())
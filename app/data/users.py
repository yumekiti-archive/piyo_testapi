def main():
  data = []

  for i in range(1, 5):
    data.append({
      'id': i,
      'name': 'John Doe',
      'email': 'hoge@hoge.hoge',
      'password': '00000000-0000-0000-0000-000000000000',
      'driver': False,
      'serial_number': '00000000-0000-0000-0000-000000000000',
      'createdAt': '2020-01-01 00:00:00',
    })

  return data

if __name__ == "__main__":
  print(main())
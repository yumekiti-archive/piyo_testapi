def main():
  data = []

  for i in range(1, 5):
    data.append({
      'id': i,
      'name': 'John Doe',
      'status': False,
      'uuid': '00000000-0000-0000-0000-000000000000',
    })

  return data

if __name__ == "__main__":
  print(main())
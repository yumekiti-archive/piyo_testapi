def main():
  data = []

  data.append({
    'id': 1,
    'start': '00:00',
    'end': '00:00',
    'createdAt': '2020-01-01 00:00:00',
  })

  for i in range(2, 10):
    data.append({
      'id': i,
      'start': '00:00',
      'end': '00:00',
      'createdAt': '2020-01-01 00:00:00',
    })

  return data

if __name__ == "__main__":
  print(main())
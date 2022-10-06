def main():
  data = []

  for i in range(1, 5):
    data.append({
      'id': i,
      'name': 'John Doe',
      'email': 'hoge@hoge.hoge'
    })

  return data

if __name__ == "__main__":
  print(main())
def principal():
  print("Keep it logically awesome.")

  f = open("quotes.txt","at")
  print("Introduce frase: ")
  item = input()
  f.write(str(item) + "\n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13],quotes[16])


if __name__== "__main__":
  principal()

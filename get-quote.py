import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  f.write("\nSample quote")
  #quotes = f.readlines()
  f.close()
  f = open("quotes.txt")
  #f.write("Sample quote")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[last])

if __name__== "__main__":
  primary()

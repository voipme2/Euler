def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

if __name__ == "__main__":
  gen = fibonacci()
  max_len = 0
  count = 0
  s = ""
  while len(s) < 1000:
    s = str(gen.next())
    if len(s) > max_len:
      max_len = len(s)
      print "F(%d) : %d" % (count, max_len)
    count = count + 1
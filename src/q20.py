if __name__ == "__main__":
  d = reduce(lambda r,s: int(r) + int(s), str(reduce(lambda x,y: x*y, range(101)[1:])))
  print "100!, adding all digits: %d" % d
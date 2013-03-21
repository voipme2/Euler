import euler

if __name__ == "__main__":
  paths = euler.pascal(2 * 20 + 1)[-1:][0][20]
  print "Number of paths for a 20x20 box: %s" % paths


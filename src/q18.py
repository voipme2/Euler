import sys
"""
  Run:  q18.py files/18-triangle.txt
"""
def max_tri(triangle):
  triangle.reverse()
  for r_i in range(len(triangle) - 1):
    row = triangle[r_i]
    next_row = triangle[r_i + 1]
    for i in range(len(row) - 1):
      next_row[i] += max(row[i], row[i+1])
  return triangle[-1][0]

def parse_triangle(f):
  tri = []
  for l in f:
    tri.append([int(n) for n in l.strip().split(" ") if len(n) > 0])
  return tri

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print "Need a triangle file."
  else:
    tri = parse_triangle(open(sys.argv[1]))
    print "Max: %d" % (max_tri(tri))
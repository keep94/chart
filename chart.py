import StringIO
import math

def Solve(f, lower, upper):
  if f(lower) > f(upper):
    g = lambda x: -f(x)
  else:
    g = f
  step = (upper - lower) / 2.0
  result = (upper + lower) / 2.0
  for _ in xrange(52):
    step /= 2.0
    if g(result) > 0.0:
      result -= step
    else:
      result += step
  return result

def X2Plus1(x):
  return x - 1/2.0/x - 3/8.0/x**3 - 3/16.0/x**5 - 45/128.0/x**7 - 63/256.0/x**9 - 375/1024.0/x**11

x5 = Solve(lambda x: X2Plus1(x) - 5.0, 5.0, 6.0)

def Special(x):
  x -= 1.0
  y = X2Plus1(x5**(2**x))
  return math.sqrt(math.sqrt(y - 1.0) - 1.0)

def Chart(f, start, incr, rowCount, colCount=1, xwidth=0, fwidth=0, xformat=str, fformat=str):

  def fixFormat(formatFunc):
    if isinstance(formatFunc, basestring):
      return lambda x: formatFunc % x
    return formatFunc

  def updateWidth(val, oldwidth):
    if len(val) > oldwidth:
      return val, len(val)
    return val, oldwidth

  def createGenericRow(colcount, starter, xval, fval):
    unit = xval + starter + fval + starter
    return starter + (unit*colcount)

  def createRowSpec(colCount, xspec, fspec):
    return createGenericRow(colCount, '|', xspec, fspec)

  def createHeader(colCount, xwidth, fwidth):
    return createGenericRow(colCount, '+', '-'*xwidth, '-'*fwidth)

  xformat = fixFormat(xformat)
  fformat = fixFormat(fformat)

  rowTuples = []
  rowValues = range(2*colCount)
  x = start
  for _ in xrange(rowCount):
    for i in xrange(colCount):
      rowValues[2*i], xwidth = updateWidth(
          xformat(x + incr*rowCount*i), xwidth)
      rowValues[2*i + 1], fwidth = updateWidth(
          fformat(f(x + incr*rowCount*i)), fwidth)
    rowTuples.append(tuple(rowValues))
    x += incr

  rowspec = createRowSpec(colCount, '%'+str(xwidth)+'s', '%'+str(fwidth)+'s')
  header = createHeader(colCount, xwidth, fwidth)
  output = StringIO.StringIO()
  print >>output, header
  for arow in rowTuples:
    print >>output, rowspec % arow
  print >>output, header
  result = output.getvalue()
  output.close()
  return result


# chart

Python code to create math charts

# Introduction

The library creates math charts. We use it to make a chart of f(x) where
f(0) = 0 and f(x + 1) = f(x)*f(x) + 1

# Theory

f(0) = 0

f(1) = 1 = 0^2 + 1

f(2) = 2 = 1^2 + 1

f(3) = 5 = 2^2 + 1

f(4) = 26 = 5^2 + 1

f(5) = 677 = 26^2 + 1


To make it easier to compute f(x), we compute function g such that

g(x^2) = g(x)^2 + 1

To compute g, we first move everythig over to one side giving

g(x)^2 + 1 - g(x^2) = 0

We can compute g as an infinite series one term at a time.

We start with g(x) = x, plug it in, and then figure out what term we need to add to g(x) to get rid of the largest term on the left hand side. Each time we add a term, we plug in what we have for g(x) and repeat. Doing this we get

![equation](http://www.sciweavers.org/tex2img.php?eq=g%28x%29%3dx%2d%5cfrac%7b1%7d%7b2x%7d%2d%5cfrac%7b3%7d%7b8x%5e3%7d%2d%5cfrac%7b3%7d%7b16x%5e5%7d%2d%5cfrac%7b45%7d%7b128x%5e7%7d%2d%5cfrac%7b63%7d%7b256x%5e9%7d%2d%5cfrac%7b375%7d%7b1024x%5e%7b11%7d%7d%2d%2e%2e%2e&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=)

We find a such that g(a) = 5 then

f(3) = g(a) = 5

f(4) = g(a^2) = 26

f(5) = g(a^4) = 677

f(6) = g(a^8)

and

f(3.5) = g(a^sqrt(2))

and

g(3 + x) = g(a^(2^x))

# work

We compute a chart for f(x) where 1 <= x < 2. That is all we need since
f(x+1) = f(x)*f(x) + 1.

and

f(x - 1) = sqrt(f(x) - 1)

# The python code

## chart.Special(x)

This is f(x)

## chart.X2Plus1(x)

This is g(x)

## chart.Solve(f, start, end)

chart.Solve returns x such that f(x) = 0. f is a monotonic inreasing
or decreasing function of one variable between start and end.
x must be between start and end.

```
>>> chart.Solve(lambda x: x*x - 5, 2.0, 3.0)
2.23606797749979
```

## chart.ISolve(f, iLowerInclusive, iUpperExclusive)

chart.ISolve solves discrete problems. chart.ISolve returns the smallest
integer n such that iLowerInclusive <= n < iUpperExclusive and f(n) is true.
f must have the property that if f(n) is true, then f(k) is true for all
integers k where k >= n. iLowerInclusive and iUpperExclusive must be integers
and iUpperExlusive > iLowerInclusive. If f(n) is false for all integers n
where iLowerInclusive <= n < iUpperExclusive then chart.ISolve returns
iUpperExclusive.

The following example uses chart.ISolve to find that the 12th fibonacci
numbr is the smallest 3 digit fibonacci number.

```
>>> def Fib(x):
...   if x in [1, 2]:
...     return 1
...   return Fib(x-1) + Fib(x-2)
...
>>> chart.ISolve(lambda x: Fib(x) >= 100, 1, 10)
10
>>> chart.ISolve(lambda x: Fib(x) >= 100, 1, 20)
12
>>> Fib(12)
144
```

Note that the first call to chart.ISolve returned iUpperExclusive signaling
that we needed to increase our range to find the smallest 3 digit fibonacci
number.

## chart.Chart(f, start, incr, rowCount, colCount=1, xwidth=0, fwidth=0, xformat=str, fformat=str)

chart.Chart builds a chart for f. f is a function of one variable, x;
start is the first value for x; rowCount is the number of rows in the
chart; optionally colCount is the number of columns, default is 1;
xformat and fformat format x and f respectively. These can be either a
format specification as a string or a function that converts a float to
a string; chart.Chart computes the widths of the columns automatically,
but caller can specify xwidth and fwidth to assign minimum widths to the
x and f columns of the chart.

chart.Chart returns the chart as a string.

```
>>> print chart.Chart(lambda x: x*x, 5, 2, 4)
+--+---+
| 5| 25|
| 7| 49|
| 9| 81|
|11|121|
+--+---+
```

This next example is f(x) where 1 <= x < 2

```
>>> print chart.Chart(chart.Special, 1, 0.01, 25, colCount=4, xformat='%.2f', fformat='%.4f')
+----+------+----+------+----+------+----+------+
|1.00|1.0000|1.25|1.1928|1.50|1.4123|1.75|1.6741|
|1.01|1.0074|1.26|1.2010|1.51|1.4218|1.76|1.6857|
|1.02|1.0147|1.27|1.2092|1.52|1.4314|1.77|1.6975|
|1.03|1.0222|1.28|1.2175|1.53|1.4411|1.78|1.7093|
|1.04|1.0296|1.29|1.2258|1.54|1.4509|1.79|1.7213|
|1.05|1.0371|1.30|1.2341|1.55|1.4607|1.80|1.7333|
|1.06|1.0445|1.31|1.2425|1.56|1.4706|1.81|1.7455|
|1.07|1.0521|1.32|1.2510|1.57|1.4805|1.82|1.7577|
|1.08|1.0596|1.33|1.2595|1.58|1.4906|1.83|1.7701|
|1.09|1.0672|1.34|1.2680|1.59|1.5007|1.84|1.7826|
|1.10|1.0748|1.35|1.2766|1.60|1.5109|1.85|1.7953|
|1.11|1.0824|1.36|1.2853|1.61|1.5212|1.86|1.8080|
|1.12|1.0900|1.37|1.2940|1.62|1.5315|1.87|1.8209|
|1.13|1.0977|1.38|1.3027|1.63|1.5420|1.88|1.8338|
|1.14|1.1055|1.39|1.3115|1.64|1.5525|1.89|1.8469|
|1.15|1.1132|1.40|1.3204|1.65|1.5631|1.90|1.8602|
|1.16|1.1210|1.41|1.3293|1.66|1.5738|1.91|1.8735|
|1.17|1.1288|1.42|1.3383|1.67|1.5846|1.92|1.8870|
|1.18|1.1367|1.43|1.3473|1.68|1.5954|1.93|1.9007|
|1.19|1.1446|1.44|1.3564|1.69|1.6064|1.94|1.9144|
|1.20|1.1525|1.45|1.3656|1.70|1.6174|1.95|1.9283|
|1.21|1.1605|1.46|1.3748|1.71|1.6286|1.96|1.9424|
|1.22|1.1685|1.47|1.3841|1.72|1.6398|1.97|1.9566|
|1.23|1.1766|1.48|1.3934|1.73|1.6511|1.98|1.9709|
|1.24|1.1847|1.49|1.4028|1.74|1.6626|1.99|1.9854|
+----+------+----+------+----+------+----+------+
```

This next example is the inverse function of x^x

```
>>> print chart.Chart(lambda x: chart.Solve(lambda y: y**y - x, 1.0, 5.0), 1, 1, 50, colCount=6, fformat='%.4f')
+---+------+---+------+---+------+---+------+---+------+---+------+
|  1|1.0000| 51|3.2963|101|3.6016|151|3.7761|201|3.8981|251|3.9917|
|  2|1.5596| 52|3.3051|102|3.6060|152|3.7789|202|3.9002|252|3.9934|
|  3|1.8255| 53|3.3138|103|3.6102|153|3.7818|203|3.9023|253|3.9951|
|  4|2.0000| 54|3.3223|104|3.6145|154|3.7845|204|3.9044|254|3.9967|
|  5|2.1294| 55|3.3307|105|3.6187|155|3.7873|205|3.9064|255|3.9984|
|  6|2.2318| 56|3.3388|106|3.6228|156|3.7901|206|3.9085|256|4.0000|
|  7|2.3165| 57|3.3468|107|3.6269|157|3.7928|207|3.9105|257|4.0016|
|  8|2.3884| 58|3.3547|108|3.6310|158|3.7955|208|3.9126|258|4.0033|
|  9|2.4510| 59|3.3624|109|3.6350|159|3.7982|209|3.9146|259|4.0049|
| 10|2.5062| 60|3.3700|110|3.6390|160|3.8009|210|3.9166|260|4.0065|
| 11|2.5556| 61|3.3775|111|3.6429|161|3.8036|211|3.9186|261|4.0081|
| 12|2.6003| 62|3.3848|112|3.6468|162|3.8062|212|3.9206|262|4.0097|
| 13|2.6411| 63|3.3920|113|3.6507|163|3.8089|213|3.9226|263|4.0113|
| 14|2.6785| 64|3.3991|114|3.6546|164|3.8115|214|3.9246|264|4.0129|
| 15|2.7132| 65|3.4061|115|3.6584|165|3.8141|215|3.9266|265|4.0145|
| 16|2.7454| 66|3.4129|116|3.6621|166|3.8167|216|3.9285|266|4.0160|
| 17|2.7754| 67|3.4197|117|3.6659|167|3.8192|217|3.9305|267|4.0176|
| 18|2.8037| 68|3.4263|118|3.6696|168|3.8218|218|3.9324|268|4.0192|
| 19|2.8302| 69|3.4329|119|3.6732|169|3.8243|219|3.9344|269|4.0207|
| 20|2.8553| 70|3.4393|120|3.6769|170|3.8269|220|3.9363|270|4.0223|
| 21|2.8791| 71|3.4457|121|3.6805|171|3.8294|221|3.9382|271|4.0238|
| 22|2.9016| 72|3.4519|122|3.6840|172|3.8318|222|3.9401|272|4.0254|
| 23|2.9231| 73|3.4581|123|3.6876|173|3.8343|223|3.9420|273|4.0269|
| 24|2.9436| 74|3.4641|124|3.6911|174|3.8368|224|3.9439|274|4.0284|
| 25|2.9632| 75|3.4701|125|3.6946|175|3.8392|225|3.9458|275|4.0300|
| 26|2.9820| 76|3.4760|126|3.6980|176|3.8416|226|3.9476|276|4.0315|
| 27|3.0000| 77|3.4818|127|3.7015|177|3.8441|227|3.9495|277|4.0330|
| 28|3.0173| 78|3.4876|128|3.7049|178|3.8465|228|3.9513|278|4.0345|
| 29|3.0340| 79|3.4932|129|3.7082|179|3.8489|229|3.9532|279|4.0360|
| 30|3.0500| 80|3.4988|130|3.7116|180|3.8512|230|3.9550|280|4.0375|
| 31|3.0655| 81|3.5043|131|3.7149|181|3.8536|231|3.9568|281|4.0390|
| 32|3.0804| 82|3.5098|132|3.7182|182|3.8559|232|3.9587|282|4.0405|
| 33|3.0949| 83|3.5152|133|3.7214|183|3.8583|233|3.9605|283|4.0419|
| 34|3.1089| 84|3.5205|134|3.7247|184|3.8606|234|3.9623|284|4.0434|
| 35|3.1225| 85|3.5257|135|3.7279|185|3.8629|235|3.9641|285|4.0449|
| 36|3.1356| 86|3.5309|136|3.7311|186|3.8652|236|3.9659|286|4.0463|
| 37|3.1484| 87|3.5360|137|3.7342|187|3.8675|237|3.9676|287|4.0478|
| 38|3.1608| 88|3.5410|138|3.7374|188|3.8697|238|3.9694|288|4.0492|
| 39|3.1729| 89|3.5460|139|3.7405|189|3.8720|239|3.9712|289|4.0507|
| 40|3.1846| 90|3.5509|140|3.7436|190|3.8742|240|3.9729|290|4.0521|
| 41|3.1961| 91|3.5558|141|3.7466|191|3.8764|241|3.9747|291|4.0536|
| 42|3.2072| 92|3.5606|142|3.7497|192|3.8787|242|3.9764|292|4.0550|
| 43|3.2181| 93|3.5654|143|3.7527|193|3.8809|243|3.9781|293|4.0564|
| 44|3.2287| 94|3.5701|144|3.7557|194|3.8831|244|3.9799|294|4.0578|
| 45|3.2390| 95|3.5748|145|3.7587|195|3.8852|245|3.9816|295|4.0592|
| 46|3.2491| 96|3.5794|146|3.7616|196|3.8874|246|3.9833|296|4.0606|
| 47|3.2590| 97|3.5839|147|3.7646|197|3.8896|247|3.9850|297|4.0621|
| 48|3.2686| 98|3.5884|148|3.7675|198|3.8917|248|3.9867|298|4.0635|
| 49|3.2780| 99|3.5929|149|3.7704|199|3.8939|249|3.9884|299|4.0648|
| 50|3.2873|100|3.5973|150|3.7732|200|3.8960|250|3.9901|300|4.0662|
+---+------+---+------+---+------+---+------+---+------+---+------+
```

This next example is 10^(x^(1/3))

```
>>> print chart.Chart(lambda x: 10**(x**(1.0/3.0)), 1, 1, 25, colCount=5, fformat='%.0f')
+---+------+---+------+---+------+---+------+---+------+
|  1|    10| 26|   917| 51|  5110| 76| 17212|101| 45395|
|  2|    18| 27|  1000| 52|  5401| 77| 17961|102| 47025|
|  3|    28| 28|  1088| 53|  5705| 78| 18735|103| 48702|
|  4|    39| 29|  1181| 54|  6022| 79| 19536|104| 50428|
|  5|    51| 30|  1280| 55|  6353| 80| 20364|105| 52203|
|  6|    66| 31|  1385| 56|  6697| 81| 21220|106| 54029|
|  7|    82| 32|  1496| 57|  7055| 82| 22105|107| 55906|
|  8|   100| 33|  1613| 58|  7428| 83| 23018|108| 57837|
|  9|   120| 34|  1736| 59|  7816| 84| 23962|109| 59821|
| 10|   143| 35|  1867| 60|  8220| 85| 24936|110| 61861|
| 11|   167| 36|  2004| 61|  8640| 86| 25942|111| 63958|
| 12|   195| 37|  2149| 62|  9076| 87| 26980|112| 66113|
| 13|   225| 38|  2301| 63|  9529| 88| 28052|113| 68326|
| 14|   257| 39|  2462| 64| 10000| 89| 29157|114| 70600|
| 15|   293| 40|  2630| 65| 10489| 90| 30297|115| 72936|
| 16|   331| 41|  2807| 66| 10996| 91| 31473|116| 75335|
| 17|   373| 42|  2992| 67| 11523| 92| 32686|117| 77799|
| 18|   418| 43|  3187| 68| 12069| 93| 33936|118| 80328|
| 19|   466| 44|  3391| 69| 12635| 94| 35224|119| 82925|
| 20|   518| 45|  3605| 70| 13222| 95| 36551|120| 85590|
| 21|   574| 46|  3829| 71| 13830| 96| 37919|121| 88326|
| 22|   634| 47|  4063| 72| 14460| 97| 39328|122| 91133|
| 23|   698| 48|  4308| 73| 15113| 98| 40779|123| 94013|
| 24|   766| 49|  4564| 74| 15788| 99| 42273|124| 96969|
| 25|   839| 50|  4831| 75| 16488|100| 43812|125|100000|
+---+------+---+------+---+------+---+------+---+------+

```

## chart.Chartf(f, start, incr, rowCount, colCount=1, xwidth=0, fwidth=0, xformat=str, fformat=str, output=sys.stdout)

chart.Chartf works like chart.Chart except instead of returning the chart
as a string, it writes the chart directly to a file. The caller specifies
the file using the output optional parameter. If the caller does not
set the output parameter, chart.Chartf writes the chart to stdout.

```
>>> chart.Chartf(lambda x:x*x, 1, 1, 5)
+-+--+
|1| 1|
|2| 4|
|3| 9|
|4|16|
|5|25|
+-+--+
>>> with open('out.txt', 'w') as f:
...   chart.Chartf(lambda x:x*x, 1, 1, 5, output=f)
...
>>>
```

class Ace(object):

    def test(self):
        print("test method")


a = Ace()
if a:
    print(1)
else:
    print(2)

# 0, false, '', None, [], {}, ()  if后面跟这几种参数判断会为False

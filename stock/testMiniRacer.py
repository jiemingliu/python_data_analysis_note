from py_mini_racer import MiniRacer
ctx = MiniRacer()
ctx.eval("1+1")

ctx.eval("var x = {company: 'Sqreen'}; x.company")

print(ctx.eval("'\N{HEAVY BLACK HEART}'"))

ctx.eval("var fun = () => ({ foo: 1 });")
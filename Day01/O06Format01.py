
# c style of formatting
format = "Welcome %s what a %s player"
print(format)
values = ("Sachin", "superb")
print(values)

print(format % values)
print("Welcome %s what a %s player" % ("Sachin", "superb"))

print("Welcome %s with a rating of %d for %s" % ("Sachin", 9.5, "India"))
print("Welcome %s with a rating of %.3f for %s" % ("Sachin", 9.5, "India"))
print("Welcome %s with a rating of %.3f for %s" % ("Sachin", 9.58343, "India"))
print("Welcome %s with a rating of %.3f for %s" % ("Sachin", 9, "India"))

# unix Style
from string import Template
tmpl = Template("Welcome $name what a $adj player")
res = tmpl.substitute(name="Sachin", adj="class")
print(f"res :{res}")

# python string formatting
print("-" * 60)
print("Welcome {} what a {} player".format("Sachin", "superb"))
print("Welcome {name} what a {adj} player".format(name="Sachin", adj="superb"))
print("Welcome {} with a rating of {} representing {}".format("Sachin", 9.8, "India"))
print("Welcome {name} with a rating of {rating:.3f} representing {cntry}".format(name="Sachin", rating=9.8, cntry="India"))

print("Welcome {2} what a {0} player representing {1}".format("Sachin", "class", "India"))

from math import pi, e
print("The value of PI is {pi} and Eulers constfant is {e}".format(pi=pi, e=e))
print("The value of PI is {pi:.3f} and Eulers constant is {e:.3f}".format(pi=pi, e=e))

print("-" * 60)
print("{val}\t{val}\t{val}".format(val="A"))
print("{val!s}\t{val!r}\t{val!a}".format(val="A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36789435122))

print("{num:10} Sachin".format(num=3))
print("{num:20} Sachin".format(num="Tendulkar"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
print("{pi:10.2}".format(pi = pi))
print("{pi:10.3}".format(pi = pi))
print("{pi:10.4}".format(pi = pi))

print("alignment".center(60, "-"))
print("{:>15} Tendulkar".format("Sachin"))          # right alignment
print("{:^15} Tendulkar".format("Sachin"))          # center alignment
print("{:<15} Tendulkar".format("Sachin"))          # left alignment

print("Sachin".center(60, "-"))
print("{:-^60}".format("Sachin"))

fn = "Sachin"
ln = "Tendulkar"

print("{0:-<10}\t{1:*>20}".format(fn, ln))

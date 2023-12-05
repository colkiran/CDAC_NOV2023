
#! c:\perl\bin

# for loop

for($i = 0; $i <= 10; $i++)
{
	print "$i ";
}
print "\n";

print "after loop $i \n";

print "-" x 60, "\n";

while($i > 0)
{
	print "$i ";
	$i--;
}
print "\n";

print "after :$i \n";

print "-" x 60, "\n";

do
{
	print "$i ";
	$i++;
} while($i <= 10);

print "\n";

print "-" x 60, "\n";

# $i = 11
# while($i >=0)

until ($i <= 0)
{
	print "$i ";
	$i--;
}

print "\n";

print "after :$i \n";

unless ($i > 0)
{
	print "hello world \n";
}









#! c:\perl64\bin

print "Enter a value for a :";

$a = <stdin>;

chomp $a;

print "Enter a value for b :";

$b = <stdin>;

chomp $b;

print "Enter the value for c :";

$c = <stdin>;

chomp $c;

print "\$a = $a \t \$b = $b \t \$c = $c \n";

print "-" x 60, "\n";

if ($a >= $b and $a >= $c)
{
	print "\$a is the greatest :$a \n";
} 
elsif ($b >= $a and $b >= $c)
{
	print "\$b is the greatest :$b \n";
} else {
	print "\$c is the greatest :$c \n";
}


#! c:\perl\bin

print "Enter the value for a :";

$a = <stdin>;	

print $a, "\n";

# print ref($a), "\n";

print "Enter the value for b :";

$b = <stdin>;

print "Enter the value for c :";

$c = <stdin>;

chomp($a);
chop($b);
chop($c);

print "\$a = $a \t \$b =  $b, \t \$c = $c \n";

print "-" x 60, "\n";

if ($a >= $b and  $a >= $c)
{
	print "\$a is the greatest :$a \n";
} elsif ($b >= $a and $b >= $c) {
	
	print "\$b is the greatest :$b \n";
} else {
	
	print "\$c is the greatest :$c \n";
}

print "-" x 60, "\n";

$j = "Hello World";
print "$j \n";

print "chop :", chop($j), $j,"\n";
print "chomp :", chomp($j), $j,"\n";







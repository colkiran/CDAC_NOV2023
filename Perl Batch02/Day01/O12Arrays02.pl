
#! c:\perl64\bin
$" = ", ";

@arr = (1..5);

print "\@arr :@arr \n";

$l = @arr;

print "The length of the array \@arr is $l \n";

print "The index of the last elemt in the array \@arr is $#arr \n";

$arr[15] = 10;

print "\@arr :@arr \n";

print "-" x 60 , "\n";

@arr = (1..10);

for ($i = 0; $i <= $#arr; $i++)
{
	print "$arr[$i] \n";
}

#print "\n";

print "-" x 60 , "\n";

print "@arr \n";

$arr[2] = "Three";
$arr[3] = "Four";

print "@arr \n";

print "-" x 60 , "\n";

delete $arr[2];

delete $arr[3];

print "@arr \n";





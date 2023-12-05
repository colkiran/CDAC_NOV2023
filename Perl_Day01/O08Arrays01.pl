
$" = ", ";	# responsible for interpreting arrays inside double quotes
$, = ":";   # responsible for interpreting arrays outside double quotes


@arr = (1, 2, 3, 'four', 'five', 'six', 7.2, 8.1, 9.7);

print @arr, "\n";

print "-" x 60, "\n";

print "@arr \n";

print "$arr[3] \n";

print "$arr[8] \n";

print "@arr[1, 4] \n";

print "@arr[1..4] \n";

print "-" x 60, "\n";

@a = (1..10);

print "\@a :@a \n";

@b = (a..j);

print "\@b :@b \n";

@c = (a..z)[8..16];

print "\@c :@c \n";

$l = @c;		#assign an array to a scalar variable to get its length

print "Length of array c :$l \n";

# index of the last element

$lst_idx = $#c;

print "index of the last element in array \@c :$lst_idx \n";

print "-" x 60, "\n";

@arr = (1..10);

print "@arr \n";

# trying to insert

$arr[3] = 44;
$arr[5] = 66;
$arr[8] = 99;

print "\@arr :@arr\n";

print "-" x 60, "\n";

for ($i = 0; $i <= $#arr; $i++)
{
	print "$arr[$i] ";
}

print "\n";

delete $arr[3];
delete $arr[5];
delete $arr[8];

print "@arr \n";

print "-" x 60, "\n";


$arr[20] = 19;

print "@arr \n";

print "length of array \@arr :$#arr \n";


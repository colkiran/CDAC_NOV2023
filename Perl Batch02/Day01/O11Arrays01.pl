
#! c:\perl\bin
#$, = " : ";
#$" = ", ";
#----------------------

@arr = (1, 2, 3, 4, "five", "six", "seven", "Eight", 9.5, 10.3, 11,2);

print @arr, "\n";

print "-" x 60 , "\n";

print "@arr \n";

print "-" x 60 , "\n";

print $arr[3], "\n";

print "-" x 60 , "\n";

print "@arr[0, 2, 4] \n";

print "@arr[0..5] \n";

print "-" x 60 , "\n";

@arr = (1..10);

print "@arr \n";

@arr = (a..k);

print "@arr \n";

@arr = (a..z)[8..16];

print "@arr \n";

print "-" x 60 , "\n";

@arr = (0, 1, 2, 3, 4, 5);

print "@arr \n";

$i = @arr;			# length of the array

print "\$i = $i \n";

print "Index of the last element of the array \@arr is $#arr \n";		# index of the last element









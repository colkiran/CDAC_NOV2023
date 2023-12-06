
#! c:\perl64\bin

@arr = (1..10);

print "@arr \n";

$len =  push(@arr, 11);

print "@arr \n";

print "The length of the array \@arr is :$len \n";

$len = push(@arr, 12, 13, 14, 15);

print "@arr \n";

print "$len \n";

$val = pop(@arr);

print "@arr \n";

print "$val \n";

print "-" x 60, "\n";

# shift and unshift

@arr = (11..20);

print "@arr \n";

$val = shift(@arr);

print "$val \n";

print "@arr \n";

$len = unshift(@arr, 8, 9, 10, 11);

print "$len \n";

print "@arr \n";

print "-" x 60, "\n";

print "@arr \n";

# splice(array, offset, length, list)
# offset - index
# length - no of elements to be replaced
# list - list of elements

@res = splice(@arr, 3, 5, 100, 200, 300);

print "@res \n";

print "@arr \n";



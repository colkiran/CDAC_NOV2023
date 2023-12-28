
#! c:\perl64\bin

@arr = (1..10);

print "@arr \n";

$aref = \@arr;

print "The address of the array \@arr is :$aref \n";

print "The address of the array \@arr is :", \@arr, "\n";

print "The elements of the array is :@{$aref} \n";

${$aref}[10] = 11;

print "The elements of the array is :@{$aref} \n";

print "The elements of the array is :@arr \n";

print "-" x 60,  "\n";

# anonymous array
print [10, 20, 30, 40, 50], "\n";

$aref  = [10, 20, 30, 40, 50];

print "The elements of the array are :@{$aref} \n";

print ${$aref}[2], "\n";

print "-" x 60,  "\n";

@arr = (1..10, ['a', 'b', 'c', \@arr, 'd', 'e', 'f'], 11..20);

print "@arr \n";

print $arr[10], "\n";

print "@{$arr[10]} \n";


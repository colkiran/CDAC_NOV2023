
#! c:\perl64\bin

@arr = (1..15);

print "@arr \n";

$aref  = \@arr;

print "Array reference \$aref :$aref \n";

#dereference
print "The array elements are :@{$aref} \n";

print "\${$aref}[9] : ${$aref}[9]\n";

print "\@{$aref}[3..8] :@{$aref}[3..8] \n";

print "-" x 60, "\n";

# anonymous array reference
print [1, 2, 3, 4, 5], "\n";

$wkds = ["mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

print "$wkds \n";

print "@{$wkds} \n";

print "\${$wkds} :${$wkds}[2] \n";

print "-" x 60, "\n";

@ar = ("python", "perl", "ruby");

print "@ar \n";

@arr = (1..5, ["Jan", "Feb", \@ar, "Mar", "Apr"], 6..10);

print "@arr \n";

print $arr[5], "\n";

print "\@{$arr[5]} :@{$arr[5]} \n";

print "-" x 60, "\n";

print "\$arr[5] :$arr[5] \n";

print "\@{$arr[5]} :@{$arr[5]} \n";

print "\${$arr[5]}[2] :${$arr[5]}[2] \n";

print "\@{${$arr[5]}[2]} :@{${$arr[5]}[2]} \n";

print "\${${$arr[5]}[2]}[1] :${${$arr[5]}[2]}[1] \n";




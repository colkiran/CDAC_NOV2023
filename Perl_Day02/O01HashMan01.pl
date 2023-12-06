
#! c:\perl64\bin

%hsh = (1, "one", 2, "two", 3, "three", 4, "four", 5, "five");
print %hsh, "\n";

print "-" x 60, "\n";

print "\$hsh{3} :$hsh{3} \n";
print "\$hsh{5} :$hsh{5} \n";
print "\$hsh{1} :$hsh{1} \n";


print "\@hsh{1, 3, 5} - @hsh{1, 3, 5} \n";

print "-" x 60, "\n";

@k = keys(%hsh);
print "@k \n";

print "-" x 60, "\n";
@v = values(%hsh);

print "@v \n";

print "-" x 60, "\n";

for $k (keys(%hsh))
{
	print "$k => $hsh{$k} \n";
}

print "-" x 60, "\n";

# modify

$hsh{3} = undef;		# null

$hsh{6} = "Sachin";

for $k (keys(%hsh))
{
	print "$k => $hsh{$k} \n";
}

print "-" x 60, "\n";

# exists

if (exists($hsh{4}))
{
	print "the value of 4 is $hsh{4} \n";
} else {
	print "4 does not exist \n";
}

print "-" x 60, "\n";

print %hsh, "\n";

$x = %hsh;

print "$x \n";

print "-" x 60, "\n";

# delete 

delete $hsh{4};

delete $hsh{3};

print %hsh, "\n";

for $k (keys(%hsh))
{
	print "$k => $hsh{$k} \n";
}

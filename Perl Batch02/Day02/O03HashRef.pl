
#! C:\perl64\bin

%hsh = ('a' => 'apple', 'b' =>  'ball', 'c' => 'cat');

print "The elements of the hash is :", %hsh, "\n";

$href = \%hsh;

print "The address of the hash %hsh is :$href \n";

print "The elements of the hash is :", %{$href}, "\n";

print "The value of b is :${$href}{'b'} \n";

print "The value of a and c is :@{$href}{'a', 'c'} \n";

print "-" x 60,  "\n";

# anonymous hash reference
print {'name' => 'Sachin', 'age' => 34, 'runs' => 45}, "\n";

$player = {'name' => 'Sachin', 'age' => 34, 'runs' => 45};

print "The address is $player \n";

print "The hash values are :", %{$player}, "\n";

print "Name :${$player}{'name'} \n";

print "-" x 60,  "\n";

for $k(sort keys(%{$player}))
{
	print "$k => ${$player}{$k} \n";
}

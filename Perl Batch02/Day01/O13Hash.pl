
#! c:\perl64\bin

%player = ("name", "Sachin", "age", 36, "runs", 80, "opn", "Australia");

print %player, "\n";

print "%player \n";

print "Name: $player{'name'} \n";
print "Runs: $player{'runs'} \n";

print "-" x 60 , "\n";

$player{'year'} = 1998;

print %player, "\n";

print "-" x 60 , "\n";

$player{'runrate'} = undef;

print %player, "\n";

# keys

@res = keys(%player);

print "@res \n";

print "-" x 60 , "\n";

for $k(keys(%player))
{
	print "$k => $player{$k} \n";
}

 print "-" x 60 , "\n";
 
 @val = values %player;
 
 print "@val \n";
 
 

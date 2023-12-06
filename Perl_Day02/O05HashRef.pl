
#! c:\perl64\bin

%emp = ("empid", "emp-001", "empname", "Micheal", "age", 28, "dept","MKT", "loc", "hyd");

print %emp, "\n";

print "-" x  60, "\n";

for $k (keys(%emp))
{
	print "$k => $emp{$k} \n";
}

print "-" x  60, "\n";

$href = \%emp;

print $href, "\n";

print %{$href}, " \n";

print "-" x  60, "\n";

for $k (keys(%{$href}))
{
	print "$k => ${$href}{$k} \n";
}
print "-" x  60, "\n";

print "Employee Name : ${$href}{'empname'} \n";

# anything  {} is anonymous hash reference

%player = ('name'=>"sachin", "age"=>36, "runs" => {"odi1", 85, "odi2", 120, "odi3", 97}, "oppo", "Aus");

print %player, "\n";

for $k (keys(%player))
{
	print "$k => $player{$k} \n";
}

print "-" x  60, "\n";

print $player{'runs'}, "\n";

print %{$player{'runs'}}, "\n";

for $k (keys(%{$player{'runs'}}))
{
	print "$k => ${$player{'runs'}}{$k} \n";
}











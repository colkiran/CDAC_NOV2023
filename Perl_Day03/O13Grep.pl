
#! c:\perl64\bin

@arr = ('blr', 'che', 'del', 'mum', 'hyd', 'kol');

print "@arr \n";

if (grep/hyd/, @arr)
{
	$res = grep(/Hyd/, @arr);
	print "\$res :$res \n";
}
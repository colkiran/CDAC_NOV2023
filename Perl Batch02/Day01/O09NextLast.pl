
for ($i = 1; $i <= 25; $i++)
{
	if ($i > 20)
	{
		last;			# break
	}
	if ($i % 2 == 1)
	{
		next;			# continue
	}
	print "$i ";
}
print "\n";
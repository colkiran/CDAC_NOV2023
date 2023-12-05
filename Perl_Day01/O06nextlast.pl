
for ($i = 0; $i <= 25; $i++)
{
	if ($i > 20)
	{
		last;
	}
	if ($i % 2 == 0)
	{
		next;
	}
	print "$i ";
}

print "\n";
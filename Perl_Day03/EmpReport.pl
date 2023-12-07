
open(FL, "emp.csv");

%gen = ();

while ($line = readline(FL))
{
	# print $line;
	
	@k = keys(%gender);

	@line = split(",", $line);

	#print(@line);
	
	# gender 
	if (grep(/$line[1]/,@k))
	{
		$gender{$line[1]}++;
	}
	else
	{
		$gender{$line[1]} = 1; 
	}
	
	
	# Designation
	unless (grep(/$line[2]/, @desig))
	{
		$desig[$#desig + 1] = $line[2];
	}

	# Departments
	
	unless (grep(/$line[3]/, @dept))
	{
		$dept[$#dept + 1] = $line[3]; 
	}
	
	$sal += $line[4];
}


close(FL);

for $k (keys(%gender))
{
	print "$k => $gender{$k} \n";
}

print "-" x 60, "\n";

print "@desig \n";

print "-" x 60, "\n";

print "@dept \n";

print "-" x 60, "\n";

print "Sum of all salaries :$sal \n";

#! c:\perl64\bin

open(FL, "< emp.csv");

%gen = ("z" => 50);	#empty hash 

while ($line = readline(FL))
{
	#print $line;
	
	@k = keys(%gen);
	
	@line = split(",", $line);
	
	if(grep(/$line[1]/, @k))
	{
		$gen{$line[1]}++;
	}
	else
	{
		$gen{$line[1]} = 1;
	}
}

print %gen, "\n";
    
close FL;
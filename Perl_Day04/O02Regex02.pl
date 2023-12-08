
$st = "LCNO-APN-73-2023-0001";

if ($st =~  m/LCNO-(KAR|APN|TEL|TND|KER|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})/)
{

	print  "Match Found \n";
	print "$& \n";

} else {
	
	print "Match not found \n";
	
}
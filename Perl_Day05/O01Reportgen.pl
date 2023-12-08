
#!c:\perl64\bin

open(FL, "< Data.csv");

format STDOUT_TOP = 
@<<<<<	   @<<<<<<<<	@<<<<<<	   @<<<<<<<    @###
"EmpID","Empname","Desig","Salary", $% 
------     ---------    --------   --------
.

$= = 25;			# no of linez in a page

while(<FL>)
{
($eid, $ename, $desig, $sal) = split(/,/);

format STDOUT = 
@##   @<<<<<<<<<   @>>>>>>>>>>    @####.##
$eid, $ename, $desig, $sal
.


write(STDOUT);

}
close (FL);

#!c:\perl64\bin

open(FL, "< Data.csv");
open(FW, "> report.txt");

format FW_TOP = 
@<<<<<	   @<<<<<<<<	@<<<<<<	   @<<<<<<<    @###
"EmpID","Empname","Desig","Salary", $% 
------     ---------    --------   --------
.

$= = 25;			# no of linez in a page

while(<FL>)
{
($eid, $ename, $desig, $sal) = split(/,/);

format FW = 
@##   @<<<<<<<<<   @>>>>>>>>>>    @####.##
$eid, $ename, $desig, $sal
.


write(FW);

}
close(FL);
close(FW);
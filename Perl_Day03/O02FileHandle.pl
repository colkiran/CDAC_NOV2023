
#! c:\perl64\bin

open(FL, "< data.txt");

read(FL, $st, 500);

print "$st \n";

close(FL);


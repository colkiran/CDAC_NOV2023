
#! c:\perl64\bin

open FL, "< data.txt";

seek(FL, 75, 0);

print tell(FL), "\n";

seek(FL, 135, 1);

print tell(FL), "\n";

seek(FL, -50, 1);

print tell(FL), "\n";

seek(FL, 100, 2);

print tell(FL), "\n";

seek(FL, 0, 2);

print tell(FL), "\n";

close FL;



open(FL, "< data.txt");

seek(FL, 85, 0);

print tell(FL), "\n";

seek(FL, 70, 1);

read(FL, $st, 45);

print tell(FL), "\n";

print "-" x 60, "\n";

seek(FL, 200, 2);

print tell(FL), "\n";

print "-" x 60, "\n";

seek(FL, 0, 2);

print "The size of the file is : ", tell(FL) ,"\n";

print "-" x 60, "\n";

seek(FL, -10, 0);

print tell(FL), "\n";
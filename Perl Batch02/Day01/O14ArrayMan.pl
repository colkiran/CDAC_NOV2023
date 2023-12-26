
#! c:\perl64\bin

@arr = (1..5);

print "@arr \n";

print "-" x 60 , "\n";

# shift

$res = shift @arr;

print "@arr \n";

print "$res \n";

print "-" x 60 , "\n";
#unshift

$res = unshift(@arr, 0, 0.1, 0.2, 0.3, 0.4, 0.5);

print "@arr \n";

print "$res \n";

print "-" x 60 , "\n";
#pop

$res = pop @arr;

print "@arr \n";

print $res , "\n";

print "-" x 60 , "\n";
#push

$res = push @arr, 6, 7, 8, 9;

print "@arr \n";

print "$res \n";

print "-" x 60 , "\n";
#splice

@arr = (1..10);

print "@arr \n";

@res = splice(@arr, 3, 2, 100, 200);	   # Replaced

print "@arr \n";

print "@res \n";

print "-" x 60 , "\n";

# replace and delete

print "@arr \n";

@res = splice(@arr, 3, 5, 40, 50);

print "@arr \n";

print "@res \n";

print "-" x 60 , "\n";
# delete
@arr = (1..10);

print "@arr \n";

@res = splice @arr, 5, 3;

print "@arr \n";

print "@res \n";

print "-" x 60 , "\n";
# insert
@arr = (1, 5);

print "@arr \n";

@res = splice @arr, 1, 0, 2, 3, 4;

print "@arr \n";

print "@res \n";



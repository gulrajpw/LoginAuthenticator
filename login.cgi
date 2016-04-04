#!/usr/bin/perl
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
	#if the login credentials match an entry in the database

my $q = CGI->new;
my $usrnme = $q->param('usrnme');
my $pass = $q->param('pass');

$entry = $usrnme . "^" . $pass;

#Open database.fdb
open(my $FH, "<", "database.fdb") or die "cannot open < database.fdb: $!";	
$message;

while(my $row = <$FH>)
{
	#if $usrnme and $pass match a row
	if($row =~ /$entry/)
	{
		$message = "Login successful \n";			
	}
	#add the blank username and password case.
	else
	{
		$message = "Credentials not found \n";
	}	
}
#close the file.
close(FH);

	#create a log of attempted or successful user access.
	#open hpl.fdb
	$date = localtime;
	open(my $hpl, ">", "hpl.fdb");
	print $hpl "\n User attempted access with credentials: $entry . $date . $ENV{REMOTE_ADDR} eith response: $message \n";
	close hpl;
	
	

			


print <<EOT;
Content-type:text/html

	<html>
		<body>
		
		$message

		</body>


	</html>

EOT

__END__



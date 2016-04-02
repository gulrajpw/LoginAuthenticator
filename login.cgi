#!/usr/bin/perl
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
	#if the login credentials match an entry in the database, log the user in
	#If they do not match, say try again, display redirects to create an account or
	#forgot password.

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
	else
	{
		$message = "Credentials not found \n";
	}	
}

print <<EOT;
Content-type:text/html

	<html>
		<body>
		
		$message

		</body>


	</html>

EOT

__END__



#!/usr/bin/perl
use warnings;
use CGI;
#Once a registration is created, the information should go to
#the database with a button to return to index.cgi
my $q = CGI->new;

my $username = $q->param('usrnme');
my $password = $q->param('pass');

	
print <<EOT;
Content-type: text/html




<html>
<body background="http://www.pacifymind.net/wp-content/uploads/10334a-nature-blur-hd-picture.jpg">
<head> <title> Registration </title> </head>

<body>
<form>
<center>
<h1 style="font-family:verdana;"> Account Registration </h1>

</center>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>

	<center>
	
	<form>


		 Enter a username: <input type="text" name="usrnme"> <br>
		
		 Enter a password: <input type="text" name="pass"> <br>
		<br>
	<button type="submit" value="Submit"> Submit </button>
	</form>
	</center>



		
	<br>
	<br>

</form>
<form action= index.cgi>
<center>
<button type="submit" value="redirect"> Back to Login </button>
</center>
</form>





</body>



</html>


EOT
	
	open(MYFILE, '>>database.fdb');

	$entry = "$username". "^" . "$password";
	

        print MYFILE "$username". "^" . "$password" . "\n";
        close(MYFILE);
	
	#encrypt the file.



__EOT__

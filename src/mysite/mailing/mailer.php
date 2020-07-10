<?php

// LOAD CONFIG
$config = parse_ini_file('config.ini.php', TRUE);



// INITIALIZE EMAILING DEFAULTS
$_FROM_NAME = $config['name'];
$_FROM_EMAIL = $config['username'].'@gmail.com';
$_FROM_USERNAME = $config['username'];
$_FROM_PASSWORD = $config['password'];
// $_BCC = $config['bcc'];
//Uncomment above for Blind CC


// EMAIL OBJECT AND ITS SETTINGS
require_once('phpmailer/class.phpmailer.php');

// START DATABASE CONNECTION
$table = $config['username'];
try
{
	$conn = new PDO("mysql:host=localhost;dbname=soze",'root','');
	$conn->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
	$sql1 = $conn->prepare("SELECT * FROM ". $table ." WHERE status=:status");
	$sql2 = $conn->prepare("UPDATE " . $table . " SET status=1 WHERE email=:email");
}
catch(Exception $e)
{
	print $e->getMessage();
}
// CHECK FOR THE DATA WITH PENDING STATUS
$data1 = array('status' => 0);
$sql1 -> setFetchMode(PDO::FETCH_ASSOC);
$sql1->execute($data1);

$count = 0;

if($sql1->rowCount() >=1)
{
	foreach($sql1 as $result)
	{
		if($count < 11000)
		{
			$name = $result['name'];
			$email = $result['email'];
			$namecheck = $result['namecheck'];
			
			$data2 = array('email'=>$email);
			try
			{
				$sql2->execute($data2); //UPDATE THE STATUS OF THE DATA
				
				include('data/letter.php');
				
				$_TO_EMAIL = $email;
				$_TO_NAME = $name;
				
				
				$mail             = new PHPMailer();

				$mail->IsSMTP(); // telling the class to use SMTP
				$mail->SMTPDebug;
				$mail->SMTPAuth   = true;                  // enable SMTP authentication
				$mail->SMTPSecure = "tls";
				$mail->Host       = "smtp.gmail.com"; // sets the SMTP server
				$mail->Port       = 587;                    // set the SMTP port for the GMAIL server
				$mail->Username   = $_FROM_USERNAME; // SMTP account username
				$mail->Password   = $_FROM_PASSWORD;        // SMTP account password

				$mail->SetFrom($_FROM_EMAIL, $_FROM_NAME);
				// $mail->AddReplyTo($_BCC, $_FROM_NAME);
				//Uncomment for BCC
				
				$mail->Subject= "IITH Water Management Report";
				$mail->Body = $letter;
				$mail->AddAddress($_TO_EMAIL, $_TO_NAME);
				//$mail->AddBCC($_BCC, $_FROM_NAME);   
				$mail->AddAttachment('data/' . $config['attachment']);

				if(!$mail->Send())
				{
				  print $email . " <font color='red'><b>FAILED</b></font><br>";
				}
				else
				{
				  print $email . " <font color='green'><b>SUCCESS</b></font><br>";
				  $count++;
				}
			}
			catch(Exception $e)
			{
				print $result['email'] . " <font color='red'><b>FAILED</b></font><br>";
			}
		}
	}
}

print "<hr><h2>" . $count . " mails sent.</h2>";
?>
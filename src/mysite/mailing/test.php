<?php

$config = parse_ini_file('config.ini.php', TRUE);

$_FROM_NAME = $config['name'];
$_FROM_EMAIL = $config['username'].'@gmail.com';
$_FROM_USERNAME = $config['username'];
$_FROM_PASSWORD = $config['password'];
// $_BCC = $config['bcc'];

$_TO_NAME = $config['name'];
// $_TO_EMAIL = $config['bcc'];

$name = "TEST NAME";
$namecheck = "TEST MAIL";
include('data/letter.php');


require_once('phpmailer/class.phpmailer.php');
//include("class.smtp.php"); // optional, gets called from within class.phpmailer.php if not already loaded

$mail             = new PHPMailer();

$body             = $letter;

$mail->IsSMTP(); // telling the class to use SMTP
$mail->SMTPDebug=1;
$mail->SMTPAuth   = true;
$mail->SMTPSecure="tls";
$mail->Host       = "smtp.gmail.com"; // SMTP server
                  // enable SMTP authentication
//$mail->Host       = "smtp.cc.iitk.ac.in"; // sets the SMTP server
$mail->Port       = 587;                    // set the SMTP port for the GMAIL server
$mail->Username   = $_FROM_USERNAME; // SMTP account username
$mail->Password   = $_FROM_PASSWORD;        // SMTP account password

$mail->SetFrom($_FROM_EMAIL, $_FROM_NAME);

// $mail->AddReplyTo($_BCC,$_FROM_NAME);

$mail->Subject    = "IIITH Water Management Report";

//$mail->MsgHTML($body);
$mail->Body = $body;

$mail->AddAddress("rajputsaransh007@gmail.com","Saransh");
$mail->AddAttachment('data/'. $config['attachment']);

if(!$mail->Send()) {
  echo "Mailer Error: " . $mail->ErrorInfo;
} else {
  echo "<h2>TEST MAIL SUCCESSFULLY SENT</h2>";
}

?>
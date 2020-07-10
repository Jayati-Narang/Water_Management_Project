<?php

$config = parse_ini_file('config.ini.php', TRUE);
$table = $config['username'];

try
{
	$conn = new PDO("mysql:host=localhost;dbname=soze",'root','');
	$conn->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION );
	$sql1 = $conn->prepare("SELECT * FROM ". $table ." WHERE email=:email"); 
	$sql2 = $conn->prepare("INSERT INTO ". $table ." (name, email, namecheck, status) value (:name, :email, :namecheck, :status)"); 
}
catch(Exception $e)
{
	print $e->getMessage();
}

$row = 0;
$total = 0;

if (($handle = fopen("data/regusers.csv", "r")) !== FALSE) 
{
    while (($data = fgetcsv($handle, ",")) !== FALSE) 
	{
		$total++;
		$data2['name'] = $data[0];
		$temp = $data[2];
		$temp1 = explode(';', $temp);
		$temp1 = explode(',',$temp1[0]);
		$data2['namecheck'] = $temp1[0];
		
		$temp2 = explode('email: ',$temp);
		if(isset($temp2[1]))
		{
		try
		{
			$data2['email'] = $temp2[1];
			$data2['status'] = 0;
				$data1['email'] = $data2['email'];
				$result = $sql1->execute($data1);
				if($sql1->rowCount() == 0)
				{
					$sql2->execute($data2);
					//var_dump($data2);
					$row++;
				}
				else
				{
					print "<b>" . $data1['email'] . '</b> <font color="red">already present</font><br>';
				}
			}
			catch(Exception $e)
			{
				print $e->getMessage() . " (" . $data2['email'] . " was not inserted)<br><br>";
			}
			
		}
    }
    fclose($handle);
	
	echo "<hr><h2>" . $row . " / " . $total . " entries successfully processed</h2>";
}
?>
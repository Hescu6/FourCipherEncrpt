<html>
<head>
<title>Four Square Cipher Encryptor</title>
<link rel="stylesheet" href="cipher.css" />
<head>
<body>

    <form action="http://localhost:1234/cypherin.php" method="post">
    <h1><br><br>Four Square cipher Encoder-Decoder</h1>

    <p><br>Please input two random keys with which the message will be encoded and decoded
    <br><br></p>


    <p>Key #1: 
    <input type = "text" name="key1" size="30" value=""  placeholder="Enter any random text" />
    </p>

    <p>Key #2: 
    <input type = "text" name="key2" size="30" value="" placeholder="Enter any random text" />
    </p>

    <p>Message: 
    <input type = "text" name="msg" size="30" value="" placeholder="Enter a message" />
    </p>

    <p>
        <input type="submit" name="submit" value="Send" />
    </p>

    </form>
    

<?php

$pyscript = 'C:\\xampp\\htdocs\\cipher.py';
$python = 'C:\\Python\\Python37\\python.exe';

$key1 = $_POST['key1'];
$key2 = $_POST['key2'];
$msg = $_POST['msg'];
$message = str_replace(' ', '', $msg);



$cmd = "$python $pyscript '$key1' '$key2' '$message'";
#$values= "'$key1' '$key2' '$msg'";

echo'<br><br><b>Original Message:</b>' . $msg . 
    '<br><br><b>Key 1:</b>' . $key1 .
    '<br><br><b>Key 1:</b>' . $key2 . '<br>';

echo shell_exec($cmd);
    /*
    $result = exec($cmd);
    echo $result;
    $result_array = json_decode($result);
    
    foreach($result_array as $row) {
        echo $row. "<br>";
    }*/
?>
<p><br><br>Learn more about Four Square Cipher encryption 
    <a href="http://practicalcryptography.com/ciphers/four-square-cipher/" target="_blank">here</a>
    </p>
</body>
</html>


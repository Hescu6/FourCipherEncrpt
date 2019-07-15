<!doctype html>
<html lang="en">
<head>
    <meta charset = "utf-8">
    <title>Four Square Cipher Encryption </title>
    <style>
            body {
        line-height: .5;
        }

        html {
        box-sizing: border-box;
        }



        body {
        background: rgb(247, 247, 247);
        }

        body, input, select, textarea {
        color: rgb(34, 34, 34);
        font-family: "Lato", sans-serif;
        font-size: 13pt;
        font-weight: 400;
        line-height: 1.0em;
        }

        input[type=text], select {
        width: 30%;
        padding: 5px 15px;
        margin: 1px 3px;
        display: inline-block;
        border: 1px solid rgb(92, 5, 5);
        border-radius: 4px;
        box-sizing: border-box;
        }

        input[type=submit] {
        width: 20%;
        background-color: rgb(92, 2, 2);
        color: white;
        padding: 10px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        }

        input[type=submit]:hover {
        background-color: #b81717;
        }
    
    </style>
    

</head>
<body>

  <form action="index.php" method="post">
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

$pyscript = 'cipher.py';
$python = '/usr/bin/python3.6';

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
?>

      <p><br><br>Learn more about Four Square Cipher encryption
      <a href="http://practicalcryptography.com/ciphers/four-square-cipher/" target="_blank">here</a>
      </p>

    <!--[if lt IE 9]><script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script><![endif]-->
</body>
</html>

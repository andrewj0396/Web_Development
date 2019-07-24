<!doctype html>
<html>
<head>
  <title>Messing Around</title>
  <meta charset="utf-8">
  <meta name="description" content="html php">
  <meta name="keywords" content="php">
</head>

<body>
  <h1>To Do's</h1>

  <form action="index.php" method="POST">
      <li>Feed the cats:<input type="checkbox" name="Test0[]" value="remove"></li>
<li>Fight the power:<input type="checkbox" name="Test1[]" value="remove"></li>
<li>Kill the king:<input type="checkbox" name="Test2[]" value="remove"></li>
<li>Win the war:<input type="checkbox" name="Test3[]" value="remove"></li>
 <input type="submit" value="Done">
  </form>

  <?php
  //Edits controls
  $test = $_POST["Test0"];
  if ($test[0] == "remove"){
    shell_exec("./html_editor.py 0");
  }
  $test = $_POST["Test1"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test2"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test3"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test4"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test5"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test6"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test7"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test8"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  $test = $_POST["Test9"];
  if ($test[0] == "remove"){
    echo "It works!";
  }
  ?>
</body>
</html>

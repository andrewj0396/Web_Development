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
    <li>Walk the dog:<input type="checkbox" name="Test0[]" value="on"></li>
<li>Feed the cats:<input type="checkbox" name="Test1[]" value="on"></li>
<li>Do your laundry:<input type="checkbox" name="Test2[]" value="on"></li>
<li>Go grocery shopping:<input type="checkbox" name="Test3[]" value="on"></li>

    <input type="submit" value="Done">
  </form>

  <?php

  $test = $_POST["Test1"];
  if ($test[0] == "on"){
    echo "It works!";
  }

  ?>

</body>
</html>

<!doctype html>
<html>
<head>
  <title>Todo List Test</title>
  <meta charset="utf-8">
  <meta name="description" content="html php">
  <meta name="keywords" content="php">
</head>

<body>
  <h1>To Do's</h1>
<?php
  function newLine(){
    echo "\n<br>\n";
  }
  echo "<form action='submission_form.php' method='POST'>";
  newLine();
  echo "<li>Walk the dog:      <input type='checkbox' name='item[]' value='Walk the dog'></li>";
  newLine();
  echo "<li>Feed the cats:      <input type='checkbox' name='item[]' value='Feed the cats'></li>";
  newLine();
  echo "<li>Fight the power:      <input type='checkbox' name='item[]' value='Fight the power'></li>";
  newLine();
  echo "<li>Kill the king:      <input type='checkbox' name='item[]' value='Kill the king'></li>";
  newLine();
  echo "<li>Win the war:      <input type='checkbox' name='item[]' value='Win the war'></li>";
  newLine();
  echo "<input type='submit'>";
  newLine();
  echo "</form>";
  newLine();
?>
</body>
</html>


  <?php
  $item = $_POST["item"];

  /*Python has to take some value for an argument. Since python wont accept null
  values the if statements below turn the null value returned by non entries in
  the form above into the string "0" and pass that to python*/
  if($item[0] == ""){
    $item[0] = "0";
  }
  if($item[1] == ""){
    $item[1] = "0";
  }
  if($item[2] == ""){
    $item[2] = "0";
  }
  if($item[3] == ""){
    $item[3] = "0";
  }
  if($item[4] == ""){
    $item[4] = "0";
  }
/*
  echo $item[0];
  echo "\n<br>\n";
  echo $item[1];
  echo "\n<br>\n";
  echo $item[2];
  echo "\n<br>\n";
  echo $item[3];
  echo "\n<br>\n";
  echo $item[4];
  echo "\n<br>\n";
*/
  $result = shell_exec("./test.py '$item[0]' '$item[1]' '$item[2]' '$item[3]' '$item[4]'");
  echo $result;
  header('http/1.1 301 Moved Permanently');
  header('Location: index.html');
  /*
  echo $items[0];
  echo $items[1];
  echo $items[2];
  echo $items[3];
  echo $items[4];
  */
  ?>

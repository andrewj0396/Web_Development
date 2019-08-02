<?php
  $item = $_POST["item"];

  if($item[0] == "Walk the dog"){
  echo "test";
  }

  header('http/1.1 301 Moved Permanently');
  header('Location: index.php');
  ?>

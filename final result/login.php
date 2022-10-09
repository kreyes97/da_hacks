<?php
    session_start();
    session_unset();
    $output = file_get_contents("StudentsData.json");
    $decode = json_decode($output, true);
    
    if(isset($_POST['login'])) {
      $username = $_POST['email'];
      $password = $_POST['password'];
    
      for($i = 0; $i < count($decode) + 1; $i++) {
        if($decode[$i]['email'] == $username && $decode[$i]['password'] == $password) {
          header("Location: panel.html");
        
        }
        else {  
              if($i == count($decode)){
              echo "<script>alert('Invalid creds!')</script>";
               }
        }
      }
    
    }
    
?>
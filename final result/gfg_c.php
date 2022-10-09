<?php
       
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                   
    function get_data() {
        $name = $_POST['name'];
        $file_name='StudentsData'. '.json';
   
        if(file_exists("$file_name")) { 
            $current_data=file_get_contents("$file_name");
            $array_data=json_decode($current_data, true);
                               
            $extra=array(
                'name' => $_POST['name'],
                'password' => $_POST['password'],
                'email' => $_POST['email'],
            );
            $array_data[]=$extra;
            return json_encode($array_data);
        }
        else {
            $datae=array();
            $datae[]=array(
                'name' => $_POST['name'],
                'password' => $_POST['password'],
                'email' => $_POST['email'],
            );
            return json_encode($datae);   
        }
    }
  
    $file_name='StudentsData'. '.json';
      
    if(file_put_contents("$file_name", get_data())) {
          header("Location: login.html");
    }                
    else {
        echo 'There is some error';                
    }
}
       
?>
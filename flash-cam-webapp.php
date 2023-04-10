<!DOCTYPE html>
<html>
  <head>
    <title>FLASH CAM STATUS</title>
  </head>

  <center><h1>FLASH CAM STATUS</h1></center>


  <style>
    table,th,td {
    border: 1px solid black;
    }
  </style>


  <body>

    <?php
		

    
    // connect to server
    $serverName = "collabserver.database.windows.net";
    $connectionOptions = array(
    "Database" => "collabDataBase",
    "UID" => "collabuser",
    "PWD" => "YTc@3364"
    );  
    $conn = sqlsrv_connect($serverName, $connectionOptions);
    if ($conn === false) {
      die(print_r(sqlsrv_errors(), true));
    }
    


    // SQL query to retrieve a column from a table
    $sql = "SELECT Cam_ID,timeDelta FROM FlashVisionStatus";

    // Execute the SQL query and retrieve the column data
    $stmt = sqlsrv_query($conn, $sql);
    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }
    
    

    // Create an HTML table
    echo "<center><table></center>";
    echo "<tr><th>Cam Location</th><th>Last Active (minutes)</th></tr></thead><tbody>";

    while ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
      echo "<tr><td>" . $row['Cam_ID'] . "</td><td>" . $row['timeDelta'] . "</td></tr>";
  }

    echo "</table>";

    // Clean up resources
    sqlsrv_free_stmt($stmt);
    sqlsrv_close($conn);

	  ?>
  </body>
</html>
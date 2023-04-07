<!DOCTYPE html>



<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
        <style>
            table,th,td {
                border: 1px solid black;
            }
        </style>
    <body>

       








<center><h1>Flash Vision Status</h1></center>
<table>
<tbody>
<tr>
<th>Abercrombie-Entry-1</th>
<th>Abercrombie-Entry-2</th>
<th>Abercrombie-Exit-1</th>
<th>Abercrombie-Exit-2</th>
<th>Abercrombie-Monthly-Express</th>
<th>Egress-1</th>
<th>Ingress-1</th>
<th>Williams-St-entry-1</th>
<th>Williams-St-Exit-1</th>
<th>Williams-St-Monthly-Exit</th> 
</tr>




if (sqlsrv_has_rows($array)) {
while ($row = sqlsrv_fetch_array($array, SQLSRV_FETCH_ASSOC)) {
    
    
<?php
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
echo "Connected successfully";

// Query

$sql = "SELECT timeDelta FROM FlashVisionStatus";
$result = sqlsrv_query($conn,$sql);
if ($result === false) {
echo "error (sqlsrv_query): ".print_r(sqlsrv_errors(), true);
exit;
}

$array = sqlsrv_fetch_array(
$result);
?>


<tr>
<td><?php echo $row['timeDelta']; ?></td>
}
<td><?php print_r($array[0]) ?></td>
<td><?php print_r($array[0]) ?></td>
<td><?php print_r($array[2]) ?></td>
<td><?php print_r($array[3]) ?></td>
<td><?php print_r($array[4]) ?></td>
<td><?php print_r($array[5]) ?></td>
<td><?php print_r($array[6]) ?></td>
<td><?php print_r($array[7]) ?></td>
<td><?php print_r($array[8]) ?></td>
<td><?php print_r($array[9]) ?></td>
</tr>
}

}


</tbody>
</table>

</body>
</html>



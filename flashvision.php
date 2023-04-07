<!DOCTYPE php>



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
<?php
$server = "collabserver.database.windows.net";
$database = "collabDataBase";
$username = "collabuser";
$password = "YTc@3364";

// Connect to the database
$connection = mysqli_connect($server,$username,$password,$database);


if (!$connection) {
    die("Connection failed: " . mysqli_connect_error());
}

// Perform a database query
$query = "SELECT * FROM FlashVisionStatus";
$result = mysqli_query($connection, $query);

//$array = mysqli_fetch_array($result);

// Check if the query was successful
if (!$result) {
    die("Query failed: " . mysqli_error($connection));
}

// Loop through the query results and display them
while ($row = mysqli_fetch_assoc($result)) {
    echo "Location: " . $row["Abercrombi-Entry-1"] . "<br>";

}

// Close the database connection
mysqli_close($connection);
?>


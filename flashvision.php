<!DOCTYPE html>




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


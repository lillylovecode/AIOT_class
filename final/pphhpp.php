<?php
// 检查是否为 POST 请求
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $medicalRecordNumber = $_POST['medicalRecordNumber'];
    $patientName = $_POST['patientName'];
    $heartRate = $_POST['heartRate'];
    $systolicPressure = $_POST['systolicPressure'];
    $diastolicPressure = $_POST['diastolicPressure'];

    $servername = "localhost";
    $username = "root";
    $password = "1234";
    $database = "aidb";


    $conn = new mysqli($servername, $username, $password, $database);


    if ($conn->connect_error) {
        die("連接失敗: " . $conn->connect_error);
    }


     $sql = "INSERT INTO feedbackdata (medicalRecordNumber, patientName, heartRate,systolicPressure, diastolicPressure,timestamp)
    VALUES ('$medicalRecordNumber', '$patientName', '$heartRate','$systolicPressure', '$diastolicPressure',NOW())";


    if ($conn->query($sql) === TRUE) {
        echo "<script>alert(\"新紀錄插入成功\")</script>";


    } else {
        echo "錯誤: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
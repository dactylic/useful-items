function newpass {
    $character_list = [char]48..[char]57 + [char]65..[char]90 + [char]97..[char]122
$password_length = 8
$password_array = @()
For ($i = 0; $i -lt $password_length; $i++) {
    $password_array += $character_list | Get-Random
}
$password = -join $password_array
Write-Output $password
}

newpass

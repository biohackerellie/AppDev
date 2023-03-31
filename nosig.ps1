# Simple WinForm for adding user to security building.
## This app is specifically for assigning door access


Set-Location $PSScriptRoot

#--------------Functions-------------------------------

#Function to add user to group or remove them if $removeAccess is true
function AddOrRemoveUserFromGroup($user, $building, $tier, $removeAccess) {
	$group = "SG-$building-D-Tier-$tier"
	try {
		if ($removeAccess) {
			Remove-ADGroupMember -Identity $group -Members $user -Confirm:$false
			[System.Windows.Forms.MessageBox]::Show("User removed from $group")
		} else {
			Add-ADGroupMember -Identity $group -Members $user
			[System.Windows.Forms.MessageBox]::Show("User added to $group")
		} 
	} catch {
		[System.Windows.Forms.MessageBox]::Show("Error modifying user access: `r`n$($_.Exception.Message)")
	}
}


## Create Tier Definitions Popup window
function TierDefButton_Click{
	$message = "Security Tier Definitions:`n`n" +
						 "Tier 1 provides 24/7 access`n" +
						 "Tier 2 allows access between 5:30am - 8:00pm 7 days a week`n" +
						 "Tier 3 allows access between 5:30am - 6:30pm Mon-Fri"
	[System.Windows.Forms.MessageBox]::Show($message)
}


# Handles Add user button click to call the function

function AddUserButton_Click() {
	$user = Get-ADUser $userTextBox.Text
	$building = $buildingComboBox.SelectedItem.ToString()
	$tier = $tierCombobox.SelectedItem.ToString()
	$removeAccess = $removeAccessCheckBox.Checked

	AddOrRemoveUserFromGroup $user $building $tier $removeAccess
}

# Create User group list
function GetGroupsButton_Click() {
	$user = Get-ADUser $userTextBox.Text
	$user_groups = Get-ADPrincipalGroupMembership -Identity $user | Select-Object -ExpandProperty Name 
	$message = "Groups associated with user: `n" + ($user_groups -join "`n")
	[System.Windows.Forms.MessageBox]::Show($message)
}
#------------------Building The Gui----------------------------

# Setting up the form
Add-type -AssemblyName System.Windows.Forms
Add-type -AssemblyName System.Drawing


$iconFilePath = Join-Path $PSScriptRoot 'logo.ico'
$icon = [System.Drawing.Icon]::ExtractAssociatedIcon($iconFilePath)
$form = New-Object System.Windows.Forms.Form
$form.Icon = $icon
$form.Text = "Door Access"
$form.Width = 500
$form.Height = 300

$form.StartPosition = "CenterScreen"
$form.BackColor = [System.Drawing.Color]::DarkGray
$form.FormBorderStyle = 'Fixed3D'
$form.Font = New-Object System.Drawing.Font("Segoe UI", 11)



# Add a custom title bar control


# Add Text Box for User
$userLabel = New-Object System.Windows.Forms.Label
$userLabel.Text = "User:`nfirstname_lastname for staff`nfirstnamelastname for students"
$userLabel.Location = New-Object System.Drawing.Point(20, 20)
$userLabel.AutoSize = $true
$userLabel.TextAlign = [System.Drawing.ContentAlignment]::TopLeft

$userTextBox = New-Object System.Windows.Forms.TextBox
$userTextBox.Location = New-Object System.Drawing.Point(300, 40)
$userTextBox.Width = 150
$userTextBox.Anchor = [System.Windows.Forms.AnchorStyles]::Top -bor [System.Windows.Forms.AnchorStyles]::Left -bor [System.Windows.Forms.AnchorStyles]::Right



# Add DropDown for Building Selection
$buildingLabel = New-Object System.Windows.Forms.Label
$buildingLabel.Text = "Select The Building: "
$buildingLabel.Location = New-Object System.Drawing.Point(20, 100)
$buildingLabel.AutoSize = $true
$buildingComboBox = New-Object System.Windows.Forms.ComboBox
$buildingComboBox.Location = New-Object System.Drawing.Point(300,100)
$buildingComboBox.Width = 150
$buildingComboBox.Items.Add("SO")
$buildingComboBox.Items.Add("WE")
$buildingComboBox.Items.Add("GR")
$buildingComboBox.Items.Add("MS")
$buildingComboBox.Items.Add("HS")
$buildingComboBox.Items.Add("TR")
$buildingComboBox.Items.Add("CO")
$buildingComboBox.Items.Add("SPF")

# Add Dropdown for Door Tiers
$tierLabel = New-Object System.Windows.Forms.Label
$tierLabel.Text = "Tier: "
$tierLabel.Location = New-Object System.Drawing.Point(20, 140)
$tierLabel.AutoSize = $true
$tierCombobox = New-Object System.Windows.Forms.ComboBox
$tierCombobox.Location = New-Object System.Drawing.Point(300, 140)
$tierCombobox.Width = 150
$tierCombobox.Items.Add("1")
$tierCombobox.Items.Add("2")
$tierCombobox.Items.Add("3")

# Add "Add User" Button
$addButton = New-Object System.Windows.Forms.Button
$addButton.Text = "Assign Access"
$addButton.Location = New-Object System.Drawing.Point(300, 180)
$addButton.Width = 150
$addButton.Add_Click({AddUserButton_Click})
$form.AcceptButton = $addButton

# Add Remove access checkbox
$removeAccessCheckBox = New-Object System.Windows.Forms.Checkbox
$removeAccessCheckBox.Text= "Check box to remove`n access instead of add"
$removeAccessCheckBox.Location = New-Object System.Drawing.Point(300, 210)
$removeAccessCheckBox.AutoSize = $true

# Add Current Groups Button
$getGroupsButton = New-Object System.Windows.Forms.Button
$getGroupsButton.Text = "View User's Groups"
$getGroupsButton.Location = New-Object System.Drawing.Point(20, 210)
$getGroupsButton.Add_Click({GetGroupsButton_Click})
$getGroupsButton.Width = 150

# Add Tier Definition Button
$tierDefButton = New-Object System.Windows.Forms.Button
$tierDefButton.Text = "Tier Descriptions"
$tierDefButton.Location = New-Object System.Drawing.Point(20, 180)
$tierDefButton.Width = 150
$tierDefButton.Add_Click({TierDefButton_Click})

# Form Controls

$form.Controls.Add($userLabel)
$form.Controls.Add($userTextBox)
$form.Controls.Add($buildingLabel)
$form.Controls.Add($buildingComboBox)
$form.Controls.Add($tierLabel)
$form.Controls.Add($tierCombobox)
$form.Controls.Add($addButton)
$form.Controls.Add($tierDefButton)
$form.Controls.Add($removeAccessCheckBox)
$form.Controls.Add($getGroupsButton)

# Display form
$result = $form.ShowDialog()
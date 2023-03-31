# Gui App for AD User Security Group Management

A simple gui app allowing users without CLI or AD experience to add users to security groups.

The app:
1. Finds an AD user
2. Can list what groups they are in
3. Add or remove users from a predetermined selection of groups. All of our security groups have a building label and a tier label. This app neatly makes them easily selectable for the user and appends them into the full group name string in PS.
4. Optional definition to explain tier levels.
5. Runs in a WinForm Gui

In my example, we are using this function to add users to security groups to define security badge access to different buildings. 


## A collection of default keybindings for VS Code on Mac, Windows and Linux. 

A list of the default keybindings for VS Code is surprisingly hard to find, even in the VS Code source, so I collected them all here. I've also included `negative` keybindings, which unmap the keybindings.


You may find these useful if you switch platforms and want your old key map back, although it's likely that you will run into conflicts with system shortcuts. 

To use them, Open up "Keyboard Shortcuts (JSON)", paste the `negative` keybindings for your current platform, then the keybindings for the platform you want. E.g. If you're on a mac and want linux keys, copy the values from `macos.negative.keybindings.json` and paste them in your keyboard shortcuts, then copy and paste everything in `linux.keybindings.json`. 


If the latest keybindings for your OS are missing, let me know, or open a PR!  
Use Quick Open (ctrl+P on Windows and Linux, cmd+P on Mac) and type in Open Default Keyboard Shortcuts (JSON).
Copy the contents of the file that is opened and paste them into your OS mapping file (e.g. windows.keybindings.json), replacing the contents. From there, you can simply open a PR, I usually run `sed` to add the negative keybindings.


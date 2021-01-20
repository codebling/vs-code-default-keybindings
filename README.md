## A collection of default keybindings for VS Code on Mac, Windows and Linux. 

A list of the default keybindings for VS Code is surprisingly hard to find, even in the VS Code source, so I collected them all here. I've also included `negative` keybindings, which unmap the keybindings.


You may find these useful if you switch platforms and want your old key map back, although it's likely that you will run into conflicts with system shortcuts. 

To use them, Open up "Keyboard Shortcuts (JSON)", paste the `negative` keybindings for your current platform, then the keybindings for the platform you want. E.g. If you're on a mac and want linux keys, copy the values from `macos.negative.keybindings.json` and paste them in your keyboard shortcuts, then copy and paste everything in `linux.keybindings.json`. 


If the latest keybindings for your OS are missing, let me know, or open a PR!  

#### How to get the latest keybindings if the ones here aren't up to date (optional):

* First clone this repo, e.g. `git clone https://github.com/codebling/vs-code-default-keybindings.git`

* Then create two empty directories, `empty1` and `empty2`

* Linux

    * In a terminal, run `code --extensions-dir "/path/to/empty1" --user-data-dir "/path/to/empty2"` using the paths to the directories you made earlier. 

* Windows

    * In the command line, run `"C:\Program Files\Microsoft VS Code\Code.exe" --extensions-dir "C:\path\to\empty1" --user-data-dir "C:\path\to\empty2"` using the paths to the directories you made earlier. 

* Mac

    * In a terminal, run
    * `export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"`
    * `code --extensions-dir "/path/to/empty1" --user-data-dir "/path/to/empty2"` using the paths to the directories you made earlier. 

* Now an instance of VSCode will appear that has no extensions loaded.

* Use Quick Open (ctrl+shift+P on Windows and Linux, cmd+shift+P on Mac) and type in Open Default Keyboard Shortcuts (JSON).

* Copy the contents of the file that is opened and paste them into a file named `vs-code-default-keybindings/scripts/linux.keybindings.raw.json` (or `vs-code-default-keybindings/scripts/windows.keybindings.raw.json` or `vs-code-default-keybindings/scripts/macos.keybindings.raw.json`)

* Run the python script `vs-code-default-keybindings/scripts/process_json.py`. You should see a result like `Wrote to ../linux.keybindings.json`.

* You now have an up-to-date `.keybindings.json`. Feel free to send a PR to this project.

